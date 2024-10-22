#include <tuple>

namespace intproj
{

class BaseFeature
{
public:

    virtual float compute_feature(std::tuple<float, float, bool> data) const = 0;

    virtual ~BaseFeature() {}
};




}
