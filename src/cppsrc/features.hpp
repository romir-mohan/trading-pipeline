#include "/home/runner/work/intern-project/intern-project/src/cppsrc/five_tick_volume_feature.hpp"
#include "/home/runner/work/intern-project/intern-project/src/cppsrc/number_trades_feature.hpp"
#include "/home/runner/work/intern-project/intern-project/src/cppsrc/percent_buy_feature.hpp"
#include "/home/runner/work/intern-project/intern-project/src/cppsrc/percent_sell_feature.hpp"

#include <limits>
#include <tuple>
#include <vector>

#pragma once

namespace intproj {

class Signal
{
  private:
    NTradesFeature number_trades;
    PercentBuyFeature percent_buy;
    PercentSellFeature percent_sell;
    FiveTickVolumeFeature five_tick_volume;

    float get_midprice(const std::vector<std::tuple<float, float, bool>> &trades)
    {
        float bb = std::numeric_limits<float>::min();
        float ba = std::numeric_limits<float>::max();

        for (const std::tuple<float, float, bool> &trade : trades) {
            float price = std::get<0>(trade);
            bool side = std::get<2>(trade);

            if (side) {
                bb = std::max(bb, price);
            } else {
                ba = std::min(ba, price);
            }
        }

        if (bb == std::numeric_limits<int>::min()) {
            return ba;
        } else if (ba == std::numeric_limits<int>::max()) {
            return bb;
        } else {
            return (bb + ba) / 2.0;
        }
    }

  public:
    std::tuple<std::vector<float>, float> get_features(const std::vector<std::tuple<float, float, bool>> &trades)
    {
        std::vector<float> features = {number_trades.compute_feature(trades),
            percent_buy.compute_feature(trades),
            percent_sell.compute_feature(trades),
            five_tick_volume.compute_feature(trades) };

        float midprice = get_midprice(trades);

        return std::make_tuple(features, midprice);
    }
};

}// namespace intproj