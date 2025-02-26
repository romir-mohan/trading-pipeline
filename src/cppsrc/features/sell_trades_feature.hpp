#include <tuple>
#include <vector>

#include "base_feature.hpp"

#pragma once

namespace intproj {

class Sell_Trade_Feature : public BaseFeature
{
  public:
    float compute_feature(std::vector<std::tuple<float, float, bool>> data) override
    {
        float sell_trades = 0;

        for (std::tuple<float, float, bool> &trade : data) {
            if (!std::get<2>(trade)) sell_trades++;
        }

        int total = data.size())

        return (sell_trades / total);
    }
};


}
