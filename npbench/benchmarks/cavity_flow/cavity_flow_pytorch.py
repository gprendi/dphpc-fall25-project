import torch

def build_up_b(b, rho, dt, u, v, dx, dy):
    b = b.clone()
    b[1:-1, 1:-1] = (rho * (1 / dt * ((u[1:-1, 2:] - u[1:-1, 0:-2]) / (2 * dx) +
                                       (v[2:, 1:-1] - v[0:-2, 1:-1]) / (2 * dy)) -
                             ((u[1:-1, 2:] - u[1:-1, 0:-2]) / (2 * dx))**2 - 2 *
                             ((u[2:, 1:-1] - u[0:-2, 1:-1]) / (2 * dy) *
                              (v[1:-1, 2:] - v[1:-1, 0:-2]) / (2 * dx)) -
                             ((v[2:, 1:-1] - v[0:-2, 1:-1]) / (2 * dy))**2))
    return b

def pressure_poisson(nit, p, dx, dy, b):
    @torch.compile
    def poisson_step(p, b):
        p = p.clone()
        pn = p.clone()
        
        p[1:-1, 1:-1] = (((pn[1:-1, 2:] + pn[1:-1, 0:-2]) * dy**2 +
                          (pn[2:, 1:-1] + pn[0:-2, 1:-1]) * dx**2) /
                         (2 * (dx**2 + dy**2)) - dx**2 * dy**2 /
                         (2 * (dx**2 + dy**2)) * b[1:-1, 1:-1])
        
        # Boundary conditions
        p[:, -1] = p[:, -2]  # dp/dx = 0 at x = 2
        p[0, :] = p[1, :]    # dp/dy = 0 at y = 0
        p[:, 0] = p[:, 1]    # dp/dx = 0 at x = 0
        p[-1, :] = 0         # p = 0 at y = 2
        
        return p
    
    for q in range(nit):
        p = poisson_step(p, b)
    
    return p

def cavity_flow(nx, ny, nt, nit, u, v, dt, dx, dy, p, rho, nu):
    @torch.compile
    def flow_step(u, v, p, b):
        # Clone to avoid in-place issues
        u = u.clone()
        v = v.clone()
        
        un = u.clone()
        vn = v.clone()
        
        # Build up b
        b = build_up_b(b, rho, dt, u, v, dx, dy)
        
        # Solve pressure Poisson
        p = pressure_poisson(nit, p, dx, dy, b)
        
        # Update u
        u[1:-1, 1:-1] = (un[1:-1, 1:-1] - un[1:-1, 1:-1] * dt / dx *
                         (un[1:-1, 1:-1] - un[1:-1, 0:-2]) -
                         vn[1:-1, 1:-1] * dt / dy *
                         (un[1:-1, 1:-1] - un[0:-2, 1:-1]) - dt / (2 * rho * dx) *
                         (p[1:-1, 2:] - p[1:-1, 0:-2]) + nu *
                         (dt / dx**2 *
                          (un[1:-1, 2:] - 2 * un[1:-1, 1:-1] + un[1:-1, 0:-2]) +
                          dt / dy**2 *
                          (un[2:, 1:-1] - 2 * un[1:-1, 1:-1] + un[0:-2, 1:-1])))
        
        # Update v
        v[1:-1, 1:-1] = (vn[1:-1, 1:-1] - un[1:-1, 1:-1] * dt / dx *
                         (vn[1:-1, 1:-1] - vn[1:-1, 0:-2]) -
                         vn[1:-1, 1:-1] * dt / dy *
                         (vn[1:-1, 1:-1] - vn[0:-2, 1:-1]) - dt / (2 * rho * dy) *
                         (p[2:, 1:-1] - p[0:-2, 1:-1]) + nu *
                         (dt / dx**2 *
                          (vn[1:-1, 2:] - 2 * vn[1:-1, 1:-1] + vn[1:-1, 0:-2]) +
                          dt / dy**2 *
                          (vn[2:, 1:-1] - 2 * vn[1:-1, 1:-1] + vn[0:-2, 1:-1])))
        
        # Boundary conditions for u
        u[0, :] = 0
        u[:, 0] = 0
        u[:, -1] = 0
        u[-1, :] = 1  # set velocity on cavity lid equal to 1
        
        # Boundary conditions for v
        v[0, :] = 0
        v[-1, :] = 0
        v[:, 0] = 0
        v[:, -1] = 0
        
        return u, v, p, b
    
    b = torch.zeros((ny, nx), device=u.device, dtype=u.dtype)
    
    for n in range(nt):
        u, v, p, b = flow_step(u, v, p, b)
    
    return u, v, p