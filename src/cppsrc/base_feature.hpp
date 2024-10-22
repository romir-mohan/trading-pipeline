#include <tuple>
#include <vector>

namespace intproj
{

class BaseFeature
{
public:

    virtual float compute_feature(std::vector<std::tuple<float, float, bool>> data) const = 0;

    virtual ~BaseFeature() {}
};




}
