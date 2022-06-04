#include<iostream>

std::string getOsname()
{
    #ifdef _WIN32
        return "windows";
    #elif _WIN64
        return "windows";
    #elif __APPLE__ || __MACH__
        return "mac osx";
    #elif __linux__
        return "linux";
    #elif __FreeBSD__
        return "freeBSD";
    #elif __unix || __unix__
        return "unix";
    #else
        return "other";
    #endif

}