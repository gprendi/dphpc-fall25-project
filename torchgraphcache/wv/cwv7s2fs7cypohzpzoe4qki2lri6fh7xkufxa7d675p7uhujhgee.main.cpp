
#include <torch/csrc/inductor/cpp_prefix.h>
extern "C"  void  kernel(const double* in_ptr0,
                       double* out_ptr0,
                       double* out_ptr1,
                       double* out_ptr2,
                       double* out_ptr3,
                       double* out_ptr4,
                       double* out_ptr5,
                       double* out_ptr6,
                       double* out_ptr7,
                       double* out_ptr8,
                       double* out_ptr9,
                       double* out_ptr10,
                       double* out_ptr11,
                       double* out_ptr12,
                       double* out_ptr13,
                       double* out_ptr14,
                       double* out_ptr15,
                       double* out_ptr16,
                       double* out_ptr17,
                       double* out_ptr18,
                       double* out_ptr19,
                       double* out_ptr20,
                       double* out_ptr21,
                       double* out_ptr22,
                       double* out_ptr23,
                       double* out_ptr24,
                       double* out_ptr25,
                       double* out_ptr26,
                       double* out_ptr27,
                       double* out_ptr28,
                       double* out_ptr29,
                       double* out_ptr30,
                       double* out_ptr31,
                       double* out_ptr32,
                       double* out_ptr33,
                       double* out_ptr34,
                       double* out_ptr35,
                       double* out_ptr36,
                       double* out_ptr37,
                       double* out_ptr38,
                       double* out_ptr39,
                       double* out_ptr40,
                       double* out_ptr41,
                       double* out_ptr42,
                       double* out_ptr43,
                       double* out_ptr44,
                       double* out_ptr45,
                       double* out_ptr46,
                       double* out_ptr47,
                       double* out_ptr48,
                       double* out_ptr49,
                       double* out_ptr50,
                       double* out_ptr51,
                       double* out_ptr52,
                       double* out_ptr53,
                       double* out_ptr54,
                       double* out_ptr55,
                       double* out_ptr56,
                       double* out_ptr57,
                       double* out_ptr58,
                       double* out_ptr59,
                       double* out_ptr60,
                       double* out_ptr61,
                       double* out_ptr62,
                       double* out_ptr63,
                       double* out_ptr64,
                       double* out_ptr65,
                       double* out_ptr66,
                       double* out_ptr67,
                       double* out_ptr68,
                       double* out_ptr69,
                       double* out_ptr70,
                       double* out_ptr71,
                       double* out_ptr72,
                       double* out_ptr73,
                       double* out_ptr74,
                       double* out_ptr75,
                       double* out_ptr76,
                       double* out_ptr77,
                       double* out_ptr78,
                       double* out_ptr79,
                       double* out_ptr80,
                       double* out_ptr81,
                       double* out_ptr82,
                       double* out_ptr83,
                       double* out_ptr84,
                       double* out_ptr85,
                       double* out_ptr86,
                       double* out_ptr87,
                       double* out_ptr88,
                       double* out_ptr89,
                       double* out_ptr90,
                       double* out_ptr91,
                       double* out_ptr92,
                       double* out_ptr93,
                       double* out_ptr94,
                       double* out_ptr95,
                       double* out_ptr96,
                       double* out_ptr97,
                       double* out_ptr98,
                       double* out_ptr99,
                       double* out_ptr100,
                       double* out_ptr101,
                       double* out_ptr102,
                       double* out_ptr103,
                       double* out_ptr104,
                       double* out_ptr105,
                       double* out_ptr106,
                       double* out_ptr107,
                       double* out_ptr108,
                       double* out_ptr109,
                       double* out_ptr110,
                       double* out_ptr111,
                       double* out_ptr112,
                       double* out_ptr113,
                       double* out_ptr114,
                       double* out_ptr115,
                       double* out_ptr116,
                       double* out_ptr117,
                       double* out_ptr118,
                       double* out_ptr119,
                       double* out_ptr120,
                       double* out_ptr121,
                       double* out_ptr122,
                       double* out_ptr123,
                       double* out_ptr124,
                       double* out_ptr125,
                       double* out_ptr126,
                       double* out_ptr127,
                       double* out_ptr128,
                       double* out_ptr129,
                       double* out_ptr130,
                       double* out_ptr131,
                       double* out_ptr132,
                       double* out_ptr133,
                       double* out_ptr134,
                       double* out_ptr135,
                       double* out_ptr136,
                       double* out_ptr137,
                       double* out_ptr138,
                       double* out_ptr139,
                       double* out_ptr140,
                       double* out_ptr141,
                       double* out_ptr142,
                       double* out_ptr143,
                       double* out_ptr144,
                       double* out_ptr145,
                       double* out_ptr146,
                       double* out_ptr147,
                       double* out_ptr148,
                       double* out_ptr149,
                       double* out_ptr150,
                       double* out_ptr151,
                       double* out_ptr152,
                       double* out_ptr153,
                       double* out_ptr154,
                       double* out_ptr155,
                       double* out_ptr156,
                       double* out_ptr157,
                       double* out_ptr158,
                       double* out_ptr159,
                       double* out_ptr160,
                       double* out_ptr161,
                       double* out_ptr162,
                       double* out_ptr163,
                       double* out_ptr164,
                       double* out_ptr165,
                       double* out_ptr166,
                       double* out_ptr167,
                       double* out_ptr168,
                       double* out_ptr169,
                       double* out_ptr170,
                       double* out_ptr171,
                       double* out_ptr172,
                       double* out_ptr173,
                       double* out_ptr174,
                       double* out_ptr175,
                       double* out_ptr176,
                       double* out_ptr177,
                       double* out_ptr178,
                       double* out_ptr179,
                       double* out_ptr180,
                       double* out_ptr181,
                       double* out_ptr182,
                       double* out_ptr183,
                       double* out_ptr184,
                       double* out_ptr185,
                       double* out_ptr186,
                       double* out_ptr187,
                       double* out_ptr188,
                       double* out_ptr189,
                       double* out_ptr190,
                       double* out_ptr191,
                       double* out_ptr192,
                       double* out_ptr193,
                       double* out_ptr194,
                       double* out_ptr195,
                       double* out_ptr196,
                       double* out_ptr197,
                       double* out_ptr198,
                       double* out_ptr199,
                       double* out_ptr200,
                       double* out_ptr201,
                       double* out_ptr202,
                       double* out_ptr203,
                       double* out_ptr204,
                       double* out_ptr205,
                       double* out_ptr206,
                       double* out_ptr207,
                       double* out_ptr208,
                       double* out_ptr209,
                       double* out_ptr210,
                       double* out_ptr211,
                       double* out_ptr212,
                       double* out_ptr213,
                       double* out_ptr214,
                       double* out_ptr215,
                       double* out_ptr216,
                       double* out_ptr217,
                       double* out_ptr218,
                       double* out_ptr219,
                       double* out_ptr220,
                       double* out_ptr221,
                       double* out_ptr222,
                       double* out_ptr223,
                       double* out_ptr224,
                       double* out_ptr225,
                       double* out_ptr226,
                       double* out_ptr227,
                       double* out_ptr228,
                       double* out_ptr229,
                       double* out_ptr230,
                       double* out_ptr231,
                       double* out_ptr232,
                       double* out_ptr233,
                       double* out_ptr234,
                       double* out_ptr235,
                       double* out_ptr236,
                       double* out_ptr237,
                       double* out_ptr238,
                       double* out_ptr239,
                       double* out_ptr240,
                       double* out_ptr241,
                       double* out_ptr242,
                       double* out_ptr243,
                       double* out_ptr244,
                       double* out_ptr245,
                       double* out_ptr246,
                       double* out_ptr247,
                       double* out_ptr248,
                       double* out_ptr249,
                       double* out_ptr250,
                       double* out_ptr251,
                       double* out_ptr252,
                       double* out_ptr253,
                       double* out_ptr254,
                       double* out_ptr255,
                       double* out_ptr256,
                       double* out_ptr257,
                       double* out_ptr258,
                       double* out_ptr259,
                       double* out_ptr260,
                       double* out_ptr261,
                       double* out_ptr262,
                       double* out_ptr263,
                       double* out_ptr264,
                       double* out_ptr265,
                       double* out_ptr266,
                       double* out_ptr267,
                       double* out_ptr268,
                       double* out_ptr269,
                       double* out_ptr270,
                       double* out_ptr271,
                       double* out_ptr272,
                       double* out_ptr273,
                       double* out_ptr274,
                       double* out_ptr275,
                       double* out_ptr276,
                       double* out_ptr277,
                       double* out_ptr278,
                       double* out_ptr279,
                       double* out_ptr280,
                       double* out_ptr281,
                       double* out_ptr282,
                       double* out_ptr283,
                       double* out_ptr284,
                       double* out_ptr285,
                       double* out_ptr286,
                       double* out_ptr287,
                       double* out_ptr288,
                       double* out_ptr289,
                       double* out_ptr290,
                       double* out_ptr291,
                       double* out_ptr292,
                       double* out_ptr293,
                       double* out_ptr294,
                       double* out_ptr295,
                       double* out_ptr296,
                       double* out_ptr297,
                       double* out_ptr298,
                       double* out_ptr299,
                       double* out_ptr300,
                       double* out_ptr301,
                       double* out_ptr302,
                       double* out_ptr303,
                       double* out_ptr304,
                       double* out_ptr305,
                       double* out_ptr306,
                       double* out_ptr307,
                       double* out_ptr308,
                       double* out_ptr309,
                       double* out_ptr310,
                       double* out_ptr311,
                       double* out_ptr312,
                       double* out_ptr313,
                       double* out_ptr314,
                       double* out_ptr315,
                       double* out_ptr316,
                       double* out_ptr317,
                       double* out_ptr318,
                       double* out_ptr319,
                       double* out_ptr320,
                       double* out_ptr321,
                       double* out_ptr322,
                       double* out_ptr323,
                       double* out_ptr324,
                       double* out_ptr325,
                       double* out_ptr326,
                       double* out_ptr327,
                       double* out_ptr328,
                       double* out_ptr329,
                       double* out_ptr330,
                       double* out_ptr331,
                       double* out_ptr332,
                       double* out_ptr333,
                       double* out_ptr334,
                       double* out_ptr335,
                       double* out_ptr336,
                       double* out_ptr337,
                       double* out_ptr338,
                       double* out_ptr339,
                       double* out_ptr340,
                       double* out_ptr341,
                       double* out_ptr342,
                       double* out_ptr343,
                       double* out_ptr344,
                       double* out_ptr345,
                       double* out_ptr346,
                       double* out_ptr347,
                       double* out_ptr348,
                       double* out_ptr349,
                       double* out_ptr350,
                       double* out_ptr351,
                       double* out_ptr352,
                       double* out_ptr353,
                       double* out_ptr354,
                       double* out_ptr355,
                       double* out_ptr356,
                       double* out_ptr357,
                       double* out_ptr358,
                       double* out_ptr359,
                       double* out_ptr360,
                       double* out_ptr361,
                       double* out_ptr362,
                       double* out_ptr363,
                       double* out_ptr364,
                       double* out_ptr365,
                       double* out_ptr366,
                       double* out_ptr367,
                       double* out_ptr368,
                       double* out_ptr369,
                       double* out_ptr370,
                       double* out_ptr371,
                       double* out_ptr372,
                       double* out_ptr373,
                       double* out_ptr374,
                       double* out_ptr375,
                       double* out_ptr376,
                       double* out_ptr377,
                       double* out_ptr378,
                       double* out_ptr379,
                       double* out_ptr380,
                       double* out_ptr381,
                       double* out_ptr382,
                       double* out_ptr383,
                       double* out_ptr384,
                       double* out_ptr385,
                       double* out_ptr386,
                       double* out_ptr387,
                       double* out_ptr388,
                       double* out_ptr389,
                       double* out_ptr390,
                       double* out_ptr391,
                       double* out_ptr392,
                       double* out_ptr393,
                       double* out_ptr394,
                       double* out_ptr395,
                       double* out_ptr396,
                       double* out_ptr397,
                       double* out_ptr398,
                       double* out_ptr399,
                       double* out_ptr400,
                       double* out_ptr401,
                       double* out_ptr402,
                       double* out_ptr403,
                       double* out_ptr404,
                       double* out_ptr405,
                       double* out_ptr406,
                       double* out_ptr407,
                       double* out_ptr408,
                       double* out_ptr409,
                       double* out_ptr410,
                       double* out_ptr411,
                       double* out_ptr412,
                       double* out_ptr413,
                       double* out_ptr414,
                       double* out_ptr415,
                       double* out_ptr416,
                       double* out_ptr417,
                       double* out_ptr418,
                       double* out_ptr419,
                       double* out_ptr420,
                       double* out_ptr421,
                       double* out_ptr422,
                       double* out_ptr423,
                       double* out_ptr424,
                       double* out_ptr425,
                       double* out_ptr426,
                       double* out_ptr427,
                       double* out_ptr428,
                       double* out_ptr429,
                       double* out_ptr430,
                       double* out_ptr431,
                       double* out_ptr432,
                       double* out_ptr433,
                       double* out_ptr434,
                       double* out_ptr435,
                       double* out_ptr436,
                       double* out_ptr437,
                       double* out_ptr438,
                       double* out_ptr439,
                       double* out_ptr440,
                       double* out_ptr441,
                       double* out_ptr442,
                       double* out_ptr443,
                       double* out_ptr444,
                       double* out_ptr445,
                       double* out_ptr446,
                       double* out_ptr447,
                       double* out_ptr448,
                       double* out_ptr449,
                       double* out_ptr450,
                       double* out_ptr451,
                       double* out_ptr452,
                       double* out_ptr453,
                       double* out_ptr454,
                       double* out_ptr455,
                       double* out_ptr456,
                       double* out_ptr457,
                       double* out_ptr458,
                       double* out_ptr459,
                       double* out_ptr460,
                       double* out_ptr461,
                       double* out_ptr462,
                       double* out_ptr463,
                       double* out_ptr464,
                       double* out_ptr465,
                       double* out_ptr466,
                       double* out_ptr467,
                       double* out_ptr468,
                       double* out_ptr469,
                       double* out_ptr470,
                       double* out_ptr471,
                       double* out_ptr472,
                       double* out_ptr473,
                       double* out_ptr474,
                       double* out_ptr475,
                       double* out_ptr476,
                       double* out_ptr477,
                       double* out_ptr478,
                       double* out_ptr479,
                       double* out_ptr480,
                       double* out_ptr481,
                       double* out_ptr482,
                       double* out_ptr483,
                       double* out_ptr484,
                       double* out_ptr485,
                       double* out_ptr486,
                       double* out_ptr487,
                       double* out_ptr488,
                       double* out_ptr489,
                       double* out_ptr490,
                       double* out_ptr491,
                       double* out_ptr492,
                       double* out_ptr493,
                       double* out_ptr494,
                       double* out_ptr495,
                       double* out_ptr496,
                       double* out_ptr497,
                       double* out_ptr498,
                       double* out_ptr499)
{
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(2003001LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr0[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(2001000LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr1[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1998999LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr2[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1996998LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr3[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1994997LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr4[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1992996LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr5[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1990995LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr6[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1988994LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr7[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1986993LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr8[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1984992LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr9[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1982991LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr10[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1980990LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr11[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1978989LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr12[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1976988LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr13[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1974987LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr14[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1972986LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr15[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1970985LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr16[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1968984LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr17[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1966983LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr18[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1964982LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr19[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1962981LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr20[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1960980LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr21[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1958979LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr22[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1956978LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr23[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1954977LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr24[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1952976LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr25[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1950975LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr26[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1948974LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr27[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1946973LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr28[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1944972LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr29[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1942971LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr30[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1940970LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr31[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1938969LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr32[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1936968LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr33[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1934967LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr34[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1932966LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr35[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1930965LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr36[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1928964LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr37[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1926963LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr38[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1924962LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr39[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1922961LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr40[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1920960LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr41[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1918959LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr42[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1916958LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr43[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1914957LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr44[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1912956LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr45[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1910955LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr46[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1908954LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr47[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1906953LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr48[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1904952LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr49[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1902951LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr50[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1900950LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr51[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1898949LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr52[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1896948LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr53[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1894947LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr54[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1892946LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr55[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1890945LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr56[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1888944LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr57[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1886943LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr58[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1884942LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr59[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1882941LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr60[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1880940LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr61[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1878939LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr62[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1876938LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr63[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1874937LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr64[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1872936LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr65[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1870935LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr66[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1868934LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr67[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1866933LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr68[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1864932LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr69[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1862931LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr70[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1860930LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr71[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1858929LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr72[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1856928LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr73[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1854927LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr74[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1852926LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr75[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1850925LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr76[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1848924LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr77[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1846923LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr78[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1844922LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr79[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1842921LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr80[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1840920LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr81[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1838919LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr82[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1836918LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr83[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1834917LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr84[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1832916LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr85[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1830915LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr86[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1828914LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr87[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1826913LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr88[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1824912LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr89[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1822911LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr90[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1820910LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr91[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1818909LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr92[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1816908LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr93[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1814907LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr94[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1812906LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr95[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1810905LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr96[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1808904LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr97[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1806903LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr98[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1804902LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr99[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1802901LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr100[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1800900LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr101[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1798899LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr102[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1796898LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr103[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1794897LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr104[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1792896LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr105[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1790895LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr106[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1788894LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr107[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1786893LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr108[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1784892LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr109[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1782891LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr110[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1780890LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr111[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1778889LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr112[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1776888LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr113[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1774887LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr114[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1772886LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr115[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1770885LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr116[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1768884LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr117[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1766883LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr118[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1764882LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr119[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1762881LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr120[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1760880LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr121[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1758879LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr122[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1756878LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr123[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1754877LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr124[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1752876LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr125[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1750875LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr126[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1748874LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr127[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1746873LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr128[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1744872LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr129[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1742871LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr130[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1740870LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr131[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1738869LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr132[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1736868LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr133[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1734867LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr134[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1732866LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr135[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1730865LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr136[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1728864LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr137[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1726863LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr138[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1724862LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr139[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1722861LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr140[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1720860LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr141[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1718859LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr142[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1716858LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr143[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1714857LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr144[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1712856LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr145[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1710855LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr146[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1708854LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr147[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1706853LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr148[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1704852LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr149[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1702851LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr150[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1700850LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr151[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1698849LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr152[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1696848LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr153[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1694847LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr154[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1692846LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr155[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1690845LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr156[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1688844LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr157[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1686843LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr158[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1684842LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr159[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1682841LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr160[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1680840LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr161[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1678839LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr162[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1676838LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr163[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1674837LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr164[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1672836LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr165[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1670835LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr166[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1668834LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr167[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1666833LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr168[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1664832LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr169[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1662831LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr170[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1660830LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr171[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1658829LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr172[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1656828LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr173[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1654827LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr174[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1652826LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr175[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1650825LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr176[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1648824LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr177[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1646823LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr178[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1644822LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr179[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1642821LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr180[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1640820LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr181[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1638819LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr182[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1636818LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr183[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1634817LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr184[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1632816LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr185[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1630815LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr186[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1628814LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr187[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1626813LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr188[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1624812LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr189[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1622811LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr190[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1620810LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr191[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1618809LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr192[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1616808LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr193[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1614807LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr194[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1612806LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr195[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1610805LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr196[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1608804LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr197[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1606803LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr198[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1604802LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr199[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1602801LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr200[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1600800LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr201[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1598799LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr202[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1596798LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr203[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1594797LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr204[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1592796LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr205[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1590795LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr206[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1588794LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr207[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1586793LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr208[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1584792LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr209[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1582791LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr210[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1580790LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr211[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1578789LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr212[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1576788LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr213[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1574787LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr214[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1572786LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr215[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1570785LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr216[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1568784LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr217[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1566783LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr218[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1564782LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr219[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1562781LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr220[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1560780LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr221[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1558779LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr222[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1556778LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr223[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1554777LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr224[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1552776LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr225[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1550775LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr226[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1548774LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr227[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1546773LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr228[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1544772LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr229[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1542771LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr230[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1540770LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr231[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1538769LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr232[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1536768LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr233[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1534767LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr234[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1532766LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr235[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1530765LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr236[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1528764LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr237[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1526763LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr238[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1524762LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr239[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1522761LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr240[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1520760LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr241[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1518759LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr242[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1516758LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr243[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1514757LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr244[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1512756LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr245[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1510755LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr246[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1508754LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr247[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1506753LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr248[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1504752LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr249[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1502751LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr250[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1500750LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr251[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1498749LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr252[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1496748LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr253[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1494747LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr254[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1492746LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr255[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1490745LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr256[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1488744LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr257[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1486743LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr258[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1484742LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr259[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1482741LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr260[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1480740LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr261[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1478739LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr262[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1476738LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr263[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1474737LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr264[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1472736LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr265[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1470735LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr266[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1468734LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr267[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1466733LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr268[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1464732LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr269[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1462731LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr270[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1460730LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr271[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1458729LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr272[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1456728LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr273[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1454727LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr274[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1452726LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr275[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1450725LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr276[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1448724LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr277[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1446723LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr278[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1444722LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr279[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1442721LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr280[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1440720LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr281[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1438719LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr282[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1436718LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr283[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1434717LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr284[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1432716LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr285[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1430715LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr286[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1428714LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr287[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1426713LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr288[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1424712LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr289[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1422711LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr290[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1420710LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr291[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1418709LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr292[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1416708LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr293[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1414707LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr294[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1412706LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr295[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1410705LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr296[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1408704LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr297[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1406703LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr298[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1404702LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr299[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1402701LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr300[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1400700LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr301[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1398699LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr302[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1396698LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr303[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1394697LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr304[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1392696LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr305[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1390695LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr306[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1388694LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr307[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1386693LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr308[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1384692LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr309[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1382691LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr310[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1380690LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr311[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1378689LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr312[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1376688LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr313[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1374687LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr314[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1372686LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr315[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1370685LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr316[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1368684LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr317[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1366683LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr318[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1364682LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr319[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1362681LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr320[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1360680LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr321[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1358679LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr322[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1356678LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr323[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1354677LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr324[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1352676LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr325[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1350675LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr326[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1348674LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr327[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1346673LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr328[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1344672LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr329[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1342671LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr330[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1340670LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr331[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1338669LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr332[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1336668LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr333[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1334667LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr334[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1332666LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr335[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1330665LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr336[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1328664LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr337[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1326663LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr338[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1324662LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr339[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1322661LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr340[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1320660LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr341[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1318659LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr342[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1316658LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr343[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1314657LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr344[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1312656LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr345[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1310655LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr346[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1308654LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr347[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1306653LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr348[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1304652LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr349[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1302651LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr350[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1300650LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr351[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1298649LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr352[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1296648LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr353[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1294647LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr354[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1292646LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr355[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1290645LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr356[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1288644LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr357[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1286643LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr358[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1284642LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr359[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1282641LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr360[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1280640LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr361[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1278639LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr362[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1276638LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr363[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1274637LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr364[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1272636LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr365[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1270635LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr366[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1268634LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr367[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1266633LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr368[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1264632LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr369[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1262631LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr370[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1260630LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr371[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1258629LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr372[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1256628LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr373[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1254627LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr374[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1252626LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr375[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1250625LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr376[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1248624LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr377[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1246623LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr378[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1244622LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr379[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1242621LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr380[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1240620LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr381[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1238619LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr382[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1236618LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr383[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1234617LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr384[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1232616LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr385[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1230615LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr386[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1228614LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr387[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1226613LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr388[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1224612LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr389[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1222611LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr390[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1220610LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr391[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1218609LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr392[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1216608LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr393[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1214607LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr394[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1212606LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr395[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1210605LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr396[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1208604LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr397[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1206603LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr398[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1204602LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr399[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1202601LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr400[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1200600LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr401[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1198599LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr402[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1196598LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr403[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1194597LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr404[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1192596LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr405[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1190595LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr406[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1188594LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr407[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1186593LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr408[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1184592LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr409[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1182591LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr410[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1180590LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr411[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1178589LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr412[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1176588LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr413[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1174587LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr414[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1172586LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr415[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1170585LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr416[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1168584LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr417[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1166583LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr418[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1164582LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr419[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1162581LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr420[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1160580LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr421[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1158579LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr422[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1156578LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr423[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1154577LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr424[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1152576LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr425[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1150575LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr426[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1148574LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr427[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1146573LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr428[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1144572LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr429[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1142571LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr430[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1140570LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr431[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1138569LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr432[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1136568LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr433[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1134567LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr434[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1132566LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr435[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1130565LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr436[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1128564LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr437[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1126563LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr438[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1124562LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr439[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1122561LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr440[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1120560LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr441[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1118559LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr442[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1116558LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr443[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1114557LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr444[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1112556LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr445[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1110555LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr446[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1108554LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr447[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1106553LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr448[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1104552LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr449[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1102551LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr450[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1100550LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr451[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1098549LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr452[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1096548LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr453[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1094547LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr454[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1092546LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr455[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1090545LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr456[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1088544LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr457[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1086543LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr458[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1084542LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr459[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1082541LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr460[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1080540LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr461[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1078539LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr462[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1076538LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr463[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1074537LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr464[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1072536LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr465[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1070535LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr466[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1068534LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr467[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1066533LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr468[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1064532LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr469[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1062531LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr470[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1060530LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr471[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1058529LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr472[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1056528LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr473[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1054527LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr474[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1052526LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr475[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1050525LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr476[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1048524LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr477[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1046523LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr478[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1044522LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr479[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1042521LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr480[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1040520LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr481[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1038519LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr482[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1036518LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr483[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1034517LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr484[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1032516LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr485[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1030515LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr486[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1028514LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr487[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1026513LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr488[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1024512LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr489[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1022511LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr490[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1020510LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr491[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1018509LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr492[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1016508LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr493[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1014507LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr494[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1012506LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr495[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1010505LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr496[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1008504LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr497[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1006503LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr498[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(1004502LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr499[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
}

// Python bindings to call kernel():
#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <sstream>
#include <cstdlib>

#ifndef _MSC_VER
#if __cplusplus < 202002L
// C++20 (earlier) code
// https://en.cppreference.com/w/cpp/language/attributes/likely
#define likely(x)       __builtin_expect(!!(x), 1)
#define unlikely(x)     __builtin_expect(!!(x), 0)
#endif
#else
#define likely(x) (x)
#define unlikely(x) (x)
#endif

// This is defined in guards.cpp so we don't need to import PyTorch headers that are slooow.
// We manually link it below to workaround issues with fbcode build.
static void* (*_torchinductor_pyobject_tensor_data_ptr)(PyObject* obj);

template <typename T> static inline T parse_arg(PyObject* args, size_t n) {
    static_assert(std::is_pointer_v<T>, "arg type must be pointer or long");
    return static_cast<T>(_torchinductor_pyobject_tensor_data_ptr(PyTuple_GET_ITEM(args, n)));
}
template <> inline int64_t parse_arg<int64_t>(PyObject* args, size_t n) {
    auto result = PyLong_AsSsize_t(PyTuple_GET_ITEM(args, n));
    if(unlikely(result == -1 && PyErr_Occurred()))
        throw std::runtime_error("expected int arg");
    return result;
}
template <> inline uintptr_t parse_arg<uintptr_t>(PyObject* args, size_t n) {
    auto result = PyLong_AsVoidPtr(PyTuple_GET_ITEM(args, n));
    if(unlikely(result == reinterpret_cast<void*>(-1) && PyErr_Occurred()))
        throw std::runtime_error("expected int arg");
    return reinterpret_cast<uintptr_t>(result);
}



static PyObject* kernel_py(PyObject* self, PyObject* args) {
    try {
        if(unlikely(!PyTuple_CheckExact(args)))
            throw std::runtime_error("tuple args required");
        if(unlikely(PyTuple_GET_SIZE(args) != 501))
            throw std::runtime_error("requires 501 args");
        kernel(parse_arg<double*>(args, 0), parse_arg<double*>(args, 1), parse_arg<double*>(args, 2), parse_arg<double*>(args, 3), parse_arg<double*>(args, 4), parse_arg<double*>(args, 5), parse_arg<double*>(args, 6), parse_arg<double*>(args, 7), parse_arg<double*>(args, 8), parse_arg<double*>(args, 9), parse_arg<double*>(args, 10), parse_arg<double*>(args, 11), parse_arg<double*>(args, 12), parse_arg<double*>(args, 13), parse_arg<double*>(args, 14), parse_arg<double*>(args, 15), parse_arg<double*>(args, 16), parse_arg<double*>(args, 17), parse_arg<double*>(args, 18), parse_arg<double*>(args, 19), parse_arg<double*>(args, 20), parse_arg<double*>(args, 21), parse_arg<double*>(args, 22), parse_arg<double*>(args, 23), parse_arg<double*>(args, 24), parse_arg<double*>(args, 25), parse_arg<double*>(args, 26), parse_arg<double*>(args, 27), parse_arg<double*>(args, 28), parse_arg<double*>(args, 29), parse_arg<double*>(args, 30), parse_arg<double*>(args, 31), parse_arg<double*>(args, 32), parse_arg<double*>(args, 33), parse_arg<double*>(args, 34), parse_arg<double*>(args, 35), parse_arg<double*>(args, 36), parse_arg<double*>(args, 37), parse_arg<double*>(args, 38), parse_arg<double*>(args, 39), parse_arg<double*>(args, 40), parse_arg<double*>(args, 41), parse_arg<double*>(args, 42), parse_arg<double*>(args, 43), parse_arg<double*>(args, 44), parse_arg<double*>(args, 45), parse_arg<double*>(args, 46), parse_arg<double*>(args, 47), parse_arg<double*>(args, 48), parse_arg<double*>(args, 49), parse_arg<double*>(args, 50), parse_arg<double*>(args, 51), parse_arg<double*>(args, 52), parse_arg<double*>(args, 53), parse_arg<double*>(args, 54), parse_arg<double*>(args, 55), parse_arg<double*>(args, 56), parse_arg<double*>(args, 57), parse_arg<double*>(args, 58), parse_arg<double*>(args, 59), parse_arg<double*>(args, 60), parse_arg<double*>(args, 61), parse_arg<double*>(args, 62), parse_arg<double*>(args, 63), parse_arg<double*>(args, 64), parse_arg<double*>(args, 65), parse_arg<double*>(args, 66), parse_arg<double*>(args, 67), parse_arg<double*>(args, 68), parse_arg<double*>(args, 69), parse_arg<double*>(args, 70), parse_arg<double*>(args, 71), parse_arg<double*>(args, 72), parse_arg<double*>(args, 73), parse_arg<double*>(args, 74), parse_arg<double*>(args, 75), parse_arg<double*>(args, 76), parse_arg<double*>(args, 77), parse_arg<double*>(args, 78), parse_arg<double*>(args, 79), parse_arg<double*>(args, 80), parse_arg<double*>(args, 81), parse_arg<double*>(args, 82), parse_arg<double*>(args, 83), parse_arg<double*>(args, 84), parse_arg<double*>(args, 85), parse_arg<double*>(args, 86), parse_arg<double*>(args, 87), parse_arg<double*>(args, 88), parse_arg<double*>(args, 89), parse_arg<double*>(args, 90), parse_arg<double*>(args, 91), parse_arg<double*>(args, 92), parse_arg<double*>(args, 93), parse_arg<double*>(args, 94), parse_arg<double*>(args, 95), parse_arg<double*>(args, 96), parse_arg<double*>(args, 97), parse_arg<double*>(args, 98), parse_arg<double*>(args, 99), parse_arg<double*>(args, 100), parse_arg<double*>(args, 101), parse_arg<double*>(args, 102), parse_arg<double*>(args, 103), parse_arg<double*>(args, 104), parse_arg<double*>(args, 105), parse_arg<double*>(args, 106), parse_arg<double*>(args, 107), parse_arg<double*>(args, 108), parse_arg<double*>(args, 109), parse_arg<double*>(args, 110), parse_arg<double*>(args, 111), parse_arg<double*>(args, 112), parse_arg<double*>(args, 113), parse_arg<double*>(args, 114), parse_arg<double*>(args, 115), parse_arg<double*>(args, 116), parse_arg<double*>(args, 117), parse_arg<double*>(args, 118), parse_arg<double*>(args, 119), parse_arg<double*>(args, 120), parse_arg<double*>(args, 121), parse_arg<double*>(args, 122), parse_arg<double*>(args, 123), parse_arg<double*>(args, 124), parse_arg<double*>(args, 125), parse_arg<double*>(args, 126), parse_arg<double*>(args, 127), parse_arg<double*>(args, 128), parse_arg<double*>(args, 129), parse_arg<double*>(args, 130), parse_arg<double*>(args, 131), parse_arg<double*>(args, 132), parse_arg<double*>(args, 133), parse_arg<double*>(args, 134), parse_arg<double*>(args, 135), parse_arg<double*>(args, 136), parse_arg<double*>(args, 137), parse_arg<double*>(args, 138), parse_arg<double*>(args, 139), parse_arg<double*>(args, 140), parse_arg<double*>(args, 141), parse_arg<double*>(args, 142), parse_arg<double*>(args, 143), parse_arg<double*>(args, 144), parse_arg<double*>(args, 145), parse_arg<double*>(args, 146), parse_arg<double*>(args, 147), parse_arg<double*>(args, 148), parse_arg<double*>(args, 149), parse_arg<double*>(args, 150), parse_arg<double*>(args, 151), parse_arg<double*>(args, 152), parse_arg<double*>(args, 153), parse_arg<double*>(args, 154), parse_arg<double*>(args, 155), parse_arg<double*>(args, 156), parse_arg<double*>(args, 157), parse_arg<double*>(args, 158), parse_arg<double*>(args, 159), parse_arg<double*>(args, 160), parse_arg<double*>(args, 161), parse_arg<double*>(args, 162), parse_arg<double*>(args, 163), parse_arg<double*>(args, 164), parse_arg<double*>(args, 165), parse_arg<double*>(args, 166), parse_arg<double*>(args, 167), parse_arg<double*>(args, 168), parse_arg<double*>(args, 169), parse_arg<double*>(args, 170), parse_arg<double*>(args, 171), parse_arg<double*>(args, 172), parse_arg<double*>(args, 173), parse_arg<double*>(args, 174), parse_arg<double*>(args, 175), parse_arg<double*>(args, 176), parse_arg<double*>(args, 177), parse_arg<double*>(args, 178), parse_arg<double*>(args, 179), parse_arg<double*>(args, 180), parse_arg<double*>(args, 181), parse_arg<double*>(args, 182), parse_arg<double*>(args, 183), parse_arg<double*>(args, 184), parse_arg<double*>(args, 185), parse_arg<double*>(args, 186), parse_arg<double*>(args, 187), parse_arg<double*>(args, 188), parse_arg<double*>(args, 189), parse_arg<double*>(args, 190), parse_arg<double*>(args, 191), parse_arg<double*>(args, 192), parse_arg<double*>(args, 193), parse_arg<double*>(args, 194), parse_arg<double*>(args, 195), parse_arg<double*>(args, 196), parse_arg<double*>(args, 197), parse_arg<double*>(args, 198), parse_arg<double*>(args, 199), parse_arg<double*>(args, 200), parse_arg<double*>(args, 201), parse_arg<double*>(args, 202), parse_arg<double*>(args, 203), parse_arg<double*>(args, 204), parse_arg<double*>(args, 205), parse_arg<double*>(args, 206), parse_arg<double*>(args, 207), parse_arg<double*>(args, 208), parse_arg<double*>(args, 209), parse_arg<double*>(args, 210), parse_arg<double*>(args, 211), parse_arg<double*>(args, 212), parse_arg<double*>(args, 213), parse_arg<double*>(args, 214), parse_arg<double*>(args, 215), parse_arg<double*>(args, 216), parse_arg<double*>(args, 217), parse_arg<double*>(args, 218), parse_arg<double*>(args, 219), parse_arg<double*>(args, 220), parse_arg<double*>(args, 221), parse_arg<double*>(args, 222), parse_arg<double*>(args, 223), parse_arg<double*>(args, 224), parse_arg<double*>(args, 225), parse_arg<double*>(args, 226), parse_arg<double*>(args, 227), parse_arg<double*>(args, 228), parse_arg<double*>(args, 229), parse_arg<double*>(args, 230), parse_arg<double*>(args, 231), parse_arg<double*>(args, 232), parse_arg<double*>(args, 233), parse_arg<double*>(args, 234), parse_arg<double*>(args, 235), parse_arg<double*>(args, 236), parse_arg<double*>(args, 237), parse_arg<double*>(args, 238), parse_arg<double*>(args, 239), parse_arg<double*>(args, 240), parse_arg<double*>(args, 241), parse_arg<double*>(args, 242), parse_arg<double*>(args, 243), parse_arg<double*>(args, 244), parse_arg<double*>(args, 245), parse_arg<double*>(args, 246), parse_arg<double*>(args, 247), parse_arg<double*>(args, 248), parse_arg<double*>(args, 249), parse_arg<double*>(args, 250), parse_arg<double*>(args, 251), parse_arg<double*>(args, 252), parse_arg<double*>(args, 253), parse_arg<double*>(args, 254), parse_arg<double*>(args, 255), parse_arg<double*>(args, 256), parse_arg<double*>(args, 257), parse_arg<double*>(args, 258), parse_arg<double*>(args, 259), parse_arg<double*>(args, 260), parse_arg<double*>(args, 261), parse_arg<double*>(args, 262), parse_arg<double*>(args, 263), parse_arg<double*>(args, 264), parse_arg<double*>(args, 265), parse_arg<double*>(args, 266), parse_arg<double*>(args, 267), parse_arg<double*>(args, 268), parse_arg<double*>(args, 269), parse_arg<double*>(args, 270), parse_arg<double*>(args, 271), parse_arg<double*>(args, 272), parse_arg<double*>(args, 273), parse_arg<double*>(args, 274), parse_arg<double*>(args, 275), parse_arg<double*>(args, 276), parse_arg<double*>(args, 277), parse_arg<double*>(args, 278), parse_arg<double*>(args, 279), parse_arg<double*>(args, 280), parse_arg<double*>(args, 281), parse_arg<double*>(args, 282), parse_arg<double*>(args, 283), parse_arg<double*>(args, 284), parse_arg<double*>(args, 285), parse_arg<double*>(args, 286), parse_arg<double*>(args, 287), parse_arg<double*>(args, 288), parse_arg<double*>(args, 289), parse_arg<double*>(args, 290), parse_arg<double*>(args, 291), parse_arg<double*>(args, 292), parse_arg<double*>(args, 293), parse_arg<double*>(args, 294), parse_arg<double*>(args, 295), parse_arg<double*>(args, 296), parse_arg<double*>(args, 297), parse_arg<double*>(args, 298), parse_arg<double*>(args, 299), parse_arg<double*>(args, 300), parse_arg<double*>(args, 301), parse_arg<double*>(args, 302), parse_arg<double*>(args, 303), parse_arg<double*>(args, 304), parse_arg<double*>(args, 305), parse_arg<double*>(args, 306), parse_arg<double*>(args, 307), parse_arg<double*>(args, 308), parse_arg<double*>(args, 309), parse_arg<double*>(args, 310), parse_arg<double*>(args, 311), parse_arg<double*>(args, 312), parse_arg<double*>(args, 313), parse_arg<double*>(args, 314), parse_arg<double*>(args, 315), parse_arg<double*>(args, 316), parse_arg<double*>(args, 317), parse_arg<double*>(args, 318), parse_arg<double*>(args, 319), parse_arg<double*>(args, 320), parse_arg<double*>(args, 321), parse_arg<double*>(args, 322), parse_arg<double*>(args, 323), parse_arg<double*>(args, 324), parse_arg<double*>(args, 325), parse_arg<double*>(args, 326), parse_arg<double*>(args, 327), parse_arg<double*>(args, 328), parse_arg<double*>(args, 329), parse_arg<double*>(args, 330), parse_arg<double*>(args, 331), parse_arg<double*>(args, 332), parse_arg<double*>(args, 333), parse_arg<double*>(args, 334), parse_arg<double*>(args, 335), parse_arg<double*>(args, 336), parse_arg<double*>(args, 337), parse_arg<double*>(args, 338), parse_arg<double*>(args, 339), parse_arg<double*>(args, 340), parse_arg<double*>(args, 341), parse_arg<double*>(args, 342), parse_arg<double*>(args, 343), parse_arg<double*>(args, 344), parse_arg<double*>(args, 345), parse_arg<double*>(args, 346), parse_arg<double*>(args, 347), parse_arg<double*>(args, 348), parse_arg<double*>(args, 349), parse_arg<double*>(args, 350), parse_arg<double*>(args, 351), parse_arg<double*>(args, 352), parse_arg<double*>(args, 353), parse_arg<double*>(args, 354), parse_arg<double*>(args, 355), parse_arg<double*>(args, 356), parse_arg<double*>(args, 357), parse_arg<double*>(args, 358), parse_arg<double*>(args, 359), parse_arg<double*>(args, 360), parse_arg<double*>(args, 361), parse_arg<double*>(args, 362), parse_arg<double*>(args, 363), parse_arg<double*>(args, 364), parse_arg<double*>(args, 365), parse_arg<double*>(args, 366), parse_arg<double*>(args, 367), parse_arg<double*>(args, 368), parse_arg<double*>(args, 369), parse_arg<double*>(args, 370), parse_arg<double*>(args, 371), parse_arg<double*>(args, 372), parse_arg<double*>(args, 373), parse_arg<double*>(args, 374), parse_arg<double*>(args, 375), parse_arg<double*>(args, 376), parse_arg<double*>(args, 377), parse_arg<double*>(args, 378), parse_arg<double*>(args, 379), parse_arg<double*>(args, 380), parse_arg<double*>(args, 381), parse_arg<double*>(args, 382), parse_arg<double*>(args, 383), parse_arg<double*>(args, 384), parse_arg<double*>(args, 385), parse_arg<double*>(args, 386), parse_arg<double*>(args, 387), parse_arg<double*>(args, 388), parse_arg<double*>(args, 389), parse_arg<double*>(args, 390), parse_arg<double*>(args, 391), parse_arg<double*>(args, 392), parse_arg<double*>(args, 393), parse_arg<double*>(args, 394), parse_arg<double*>(args, 395), parse_arg<double*>(args, 396), parse_arg<double*>(args, 397), parse_arg<double*>(args, 398), parse_arg<double*>(args, 399), parse_arg<double*>(args, 400), parse_arg<double*>(args, 401), parse_arg<double*>(args, 402), parse_arg<double*>(args, 403), parse_arg<double*>(args, 404), parse_arg<double*>(args, 405), parse_arg<double*>(args, 406), parse_arg<double*>(args, 407), parse_arg<double*>(args, 408), parse_arg<double*>(args, 409), parse_arg<double*>(args, 410), parse_arg<double*>(args, 411), parse_arg<double*>(args, 412), parse_arg<double*>(args, 413), parse_arg<double*>(args, 414), parse_arg<double*>(args, 415), parse_arg<double*>(args, 416), parse_arg<double*>(args, 417), parse_arg<double*>(args, 418), parse_arg<double*>(args, 419), parse_arg<double*>(args, 420), parse_arg<double*>(args, 421), parse_arg<double*>(args, 422), parse_arg<double*>(args, 423), parse_arg<double*>(args, 424), parse_arg<double*>(args, 425), parse_arg<double*>(args, 426), parse_arg<double*>(args, 427), parse_arg<double*>(args, 428), parse_arg<double*>(args, 429), parse_arg<double*>(args, 430), parse_arg<double*>(args, 431), parse_arg<double*>(args, 432), parse_arg<double*>(args, 433), parse_arg<double*>(args, 434), parse_arg<double*>(args, 435), parse_arg<double*>(args, 436), parse_arg<double*>(args, 437), parse_arg<double*>(args, 438), parse_arg<double*>(args, 439), parse_arg<double*>(args, 440), parse_arg<double*>(args, 441), parse_arg<double*>(args, 442), parse_arg<double*>(args, 443), parse_arg<double*>(args, 444), parse_arg<double*>(args, 445), parse_arg<double*>(args, 446), parse_arg<double*>(args, 447), parse_arg<double*>(args, 448), parse_arg<double*>(args, 449), parse_arg<double*>(args, 450), parse_arg<double*>(args, 451), parse_arg<double*>(args, 452), parse_arg<double*>(args, 453), parse_arg<double*>(args, 454), parse_arg<double*>(args, 455), parse_arg<double*>(args, 456), parse_arg<double*>(args, 457), parse_arg<double*>(args, 458), parse_arg<double*>(args, 459), parse_arg<double*>(args, 460), parse_arg<double*>(args, 461), parse_arg<double*>(args, 462), parse_arg<double*>(args, 463), parse_arg<double*>(args, 464), parse_arg<double*>(args, 465), parse_arg<double*>(args, 466), parse_arg<double*>(args, 467), parse_arg<double*>(args, 468), parse_arg<double*>(args, 469), parse_arg<double*>(args, 470), parse_arg<double*>(args, 471), parse_arg<double*>(args, 472), parse_arg<double*>(args, 473), parse_arg<double*>(args, 474), parse_arg<double*>(args, 475), parse_arg<double*>(args, 476), parse_arg<double*>(args, 477), parse_arg<double*>(args, 478), parse_arg<double*>(args, 479), parse_arg<double*>(args, 480), parse_arg<double*>(args, 481), parse_arg<double*>(args, 482), parse_arg<double*>(args, 483), parse_arg<double*>(args, 484), parse_arg<double*>(args, 485), parse_arg<double*>(args, 486), parse_arg<double*>(args, 487), parse_arg<double*>(args, 488), parse_arg<double*>(args, 489), parse_arg<double*>(args, 490), parse_arg<double*>(args, 491), parse_arg<double*>(args, 492), parse_arg<double*>(args, 493), parse_arg<double*>(args, 494), parse_arg<double*>(args, 495), parse_arg<double*>(args, 496), parse_arg<double*>(args, 497), parse_arg<double*>(args, 498), parse_arg<double*>(args, 499), parse_arg<double*>(args, 500)); Py_RETURN_NONE;
    } catch(std::exception const& e) {
        PyErr_SetString(PyExc_RuntimeError, e.what());
        return nullptr;
    } catch(...) {
        PyErr_SetString(PyExc_RuntimeError, "unhandled error");
        return nullptr;
    }
}

static PyMethodDef py_methods[] = {
    {"kernel", kernel_py, METH_VARARGS, ""},
    {NULL, NULL, 0, NULL}};

static struct PyModuleDef py_module =
    {PyModuleDef_HEAD_INIT, "kernel", NULL, -1, py_methods};

PyMODINIT_FUNC PyInit_kernel(void) {
    const char* str_addr = std::getenv("_TORCHINDUCTOR_PYOBJECT_TENSOR_DATA_PTR");
    if(!str_addr) {
        PyErr_SetString(PyExc_RuntimeError, "_TORCHINDUCTOR_PYOBJECT_TENSOR_DATA_PTR must be set");
        return nullptr;
    }
    std::istringstream iss(str_addr);
    uintptr_t addr = 0;
    iss >> addr;
    _torchinductor_pyobject_tensor_data_ptr =
        reinterpret_cast<decltype(_torchinductor_pyobject_tensor_data_ptr)>(addr);
    PyObject* module = PyModule_Create(&py_module);
    if (module == NULL) {
        return NULL;
    }
    #ifdef Py_GIL_DISABLED
        PyUnstable_Module_SetGIL(module, Py_MOD_GIL_NOT_USED);
    #endif
    return module;
}
