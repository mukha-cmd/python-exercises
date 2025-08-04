#include "raindrops.h"
#include <string>
// TODO: add your solution here
namespace raindrops {
    std::string convert(int a) {
        std::string result = "";

        if (a % 3 == 0) result += "Pling";
        if (a % 5 == 0) result += "Plang";
        if (a % 7 == 0) result += "Plong";

        if (result.empty()) result = std::to_string(a);
        return result;
    }
}  // namespace raindrops
