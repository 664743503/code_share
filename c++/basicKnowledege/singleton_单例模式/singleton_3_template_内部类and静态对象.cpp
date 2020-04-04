#include <iostream>

using namespace std;

template <typename Type>
class Singleton
{
private:
    class AutoRelease
    {
    public:
        AutoRelease(){cout << "AutoRelease()" << endl;}
        ~AutoRelease()
        {
            if(m_pInstance != nullptr)
            {
                delete m_pInstance;
                m_pInstance = nullptr;
                cout << "~AutoRelease()" << endl;
            }
        }
    };
public:
    template<typename... Args>//Args:模板参数包
    static Type* getInstance(Args... args)//args:函数参数包
    {
        if(m_pInstance == nullptr)
        {
            //模板只会在实例化之后，才会进行参数推导
            //所以要调用一次m_auto
            m_auto;
            m_pInstance = new Type(args...);//解函数参数包
        }
        return m_pInstance;
    }

private:
    Singleton();
    ~Singleton();

private:
    static Type* m_pInstance;
    static AutoRelease m_auto;
};

template<typename Type>
Type* Singleton<Type>::m_pInstance = nullptr;

template<typename Type>
//这里在最前面需要加class是因为无法确定AutoRelease是成员变量还是嵌套类还是成员函数
//所以显式声明为class
class Singleton<Type>::AutoRelease Singleton<Type>::m_auto;

//demo------------------------------------
class Point
{
public:
    Point(int x = 0, int y = 0)
        :m_x(x)
         ,m_y(y)
    {cout << "Point(int x, int y)" << endl;}

    ~Point(){cout << "~Point()"<< endl;}

    friend ostream & operator<<(ostream & os, const Point & rhs);
private:
    int m_x;
    int m_y;
};

ostream & operator<<(ostream & os, const Point & rhs)
{
    os << "(" << rhs.m_x << ", " << rhs.m_y << ")";
    return os;
}

int main()
{
    Point* pt1 = Singleton<Point>::getInstance(1, 2);
    Point* pt2 = Singleton<Point>::getInstance(1, 2);

    cout << static_cast<Point*>(pt1) << endl;
    cout << static_cast<Point*>(pt2) << endl;
    cout << "*pt1 = " << *pt1 << endl;
    cout << "*pt2 = " << *pt2 << endl;

    return 0;
}
