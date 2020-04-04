#include <iostream>

using namespace std;

// 下面两个类非常接近STL的实现了，唯一的差别在于缺乏“可配接能力”

template<class T>
struct Plus
{
    // 重载了operator()的类，称为仿函数
    T operator()(const T& x, const T& y) const
    {
        return x + y;
    }
};

template<class T>
struct Minus
{
    T operator()(const T& x, const T& y) const 
    {
        return x - y;
    }
};

int main()
{
    Plus<int> plusobj;
    Minus<int> minusobj;

    // 下面使用仿函数，就像使用一般函数一样
    cout << plusobj(3, 5) << endl;
    cout << minusobj(7, 4) << endl;

    // 直接产生仿函数的临时对象，并调用
    cout << Plus<int>()(5, 6) << endl;
    cout << Minus<int>()(3, 8) << endl;

    return 0;
}
