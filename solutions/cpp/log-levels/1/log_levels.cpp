#include <string>
//[INFO]: 
namespace log_line {
std::string message(std::string line) {
    if (line.find("ERROR") == 1) {
        std::string sub_message = line.substr(9);
        return sub_message;
    }
    else if (line.find("INFO") == 1){
        std::string sub_message = line.substr(8);
        return sub_message;
    }
    std::string sub_message = line.substr(11);
    return sub_message;
}
std::string log_level(std::string line) {
     if (line.find("ERROR") == 1) {
        std::string sub_log = line.substr(1, 5);
        return sub_log;
    }
    else if (line.find("INFO") == 1){
        std::string sub_log = line.substr(1, 4);
        return sub_log;
    }
    std::string sub_log = line.substr(1, 7);
    return sub_log;
}

std::string reformat(std::string line) {
    // return the reformatted message
    if (line.find("ERROR") == 1) {
        std::string sub_message = line.substr(9);
        std::string sub_log = line.substr(1, 5);
        return sub_message + " " + "(" + sub_log + ")";
    }
    else if (line.find("INFO") == 1){
        std::string sub_message = line.substr(8);
        std::string sub_log = line.substr(1, 4);
        return sub_message + " " + "(" + sub_log + ")";
    }
    std::string sub_message = line.substr(11);
    std::string sub_log = line.substr(1, 7);
    return sub_message + " " + "(" + sub_log + ")";
}
}  // namespace log_line
