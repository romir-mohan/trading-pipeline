#include <tuple>
#include <vector>

#include "base_feature.hpp"

#pragma once

namespace intproj {

class Number_Trades : public BaseFeature
{
  public:
    float compute_feature(std::vector<std::tuple<float, float, bool>> data) override
    {
        return data.size();
    }
};


}
