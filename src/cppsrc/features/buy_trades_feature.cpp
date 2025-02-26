#include <iostream>
#include <tuple>
#include <vector>

#include "base_feature.hpp"

#pragma once

namespace intproj {

class Buys_Trade_Feature : public BaseFeature
{
  public:
    float compute_feature(std::vector<std::tuple<float, float, bool>> data) override
    {
        float buy_trades = 0;

        for (std::tuple<float, float, bool> &trade : data) {
            if (std::get<2>(trade)) buy_trades++;
        }
      
        int total = data.size()
        return (buy_trades / total);
    }
};

}
