#include "/home/runner/work/intern-project/intern-project/src/cppsrc/data/signal.hpp"
#include "gtest/gtest.h"

#include <tuple>
#include <vector>

std::vector<std::tuple<float, float, bool>> sample_data_signal = { { 105.4f, 20.8f, true },
    { 110.9f, 5.2f, false },
    { 106.4f, 234.0f, true } };

TEST(SignalTests, ComputeFeaturesTest)
{
    intproj::Signal signal;

    std::tuple<std::vector<float>, float> data = signal.compute_features(sample_data_signal);

    std::vector<float> features = std::get<0>(data);
    float midprice = std::get<1>(data);

    EXPECT_EQ(features.size(), 4);
    EXPECT_EQ(features[0], 3);
    EXPECT_NEAR(features[1], 0.66666667, .000001);
    EXPECT_NEAR(features[2], 0.33333334, .000001);
    EXPECT_EQ(features[3], 260.0);

    EXPECT_EQ(midprice, 108.65f);
}