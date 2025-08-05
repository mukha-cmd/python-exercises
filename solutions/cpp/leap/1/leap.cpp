#include "leap.h"

namespace leap {
// TODO: add your solution here
    bool is_leap_year(int n){
        if (n % 400 == 0 || (n % 4 == 0 && n % 100 != 0) ){
            return true;
        }
        else {
            return false;
        }
    }
}  // namespace leap
