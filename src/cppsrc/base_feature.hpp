namespace intproj
{

class BaseFeature
{
public:

    virtual float compute_feature() const = 0;

    virtual ~BaseFeature() {}
};




}
