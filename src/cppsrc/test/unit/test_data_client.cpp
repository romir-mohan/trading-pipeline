#include "src/cppsrc/data/data_client.hpp"
#include "nlohmann/json.hpp"
#include "gtest/gtest.h"

#include <string>

std::string sample_json_unit = R"([
    {
        "timestamp": 1,
        "timestampms": 1000,
        "tid": 1,
        "price": "101",
        "amount": "30",
        "exchange": "gemini",
        "type": "sell",
    },
    {
        "timestamp": 2,
        "timestampms": 2000,
        "tid": 2,
        "price": "202",
        "amount": "20",
        "exchange": "gemini",
        "type": "buy",
    },
    {
        "timestamp": 3,
        "timestampms": 3000,
        "tid": 3,
        "price": "303.3",
        "amount": "33.3",
        "exchange": "gemini",
        "type": "sell",
    },
    {
        "timestamp": 4,
        "timestampms": 4123,
        "tid": 4,
        "price": "404.4",
        "amount": "44.4",
        "exchange": "gemini",
        "type": "buy",
    },
])";

TEST(DataClientTests, ParseMessageTest)
{
    nlohmann::json j = nlohmann::json::parse(sample_json_unit);
    intproj::DataClient data_client;

    std::vector<std::tuple<float, float, bool>> parsed = data_client.parse_message(j);

    EXPECT_EQ(parsed.size(), 3);
    EXPECT_EQ(std::get<0>(parsed[0]), 105.4f);
    EXPECT_EQ(std::get<1>(parsed[0]), 20.8f);
    EXPECT_TRUE(std::get<2>(parsed[0]));
}