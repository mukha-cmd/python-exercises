#include "darts.h"

namespace darts {

// TODO: add your solution here
    int score(double x, double y){
        double sum = x * x + y * y;
        if (sum <= 1.0)
            return 10;
        else if (sum > 1.0 && sum <= 25.0)
            return 5;
        else if (sum > 25.0 && sum <= 100.0)
            return 1;
        return 0;
    }
}  // namespace darts