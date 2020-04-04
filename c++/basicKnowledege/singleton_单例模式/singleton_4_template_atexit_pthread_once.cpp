#include <iostream>
#include <pthread.h>

using namespace std;

class Noncopyable
{
protected:
	Noncopyable() = default;
	~Noncopyable() = default;
private:
	Noncopyable(const Noncopyable&) = delete;
	const Noncopyable& operator=( const Noncopyable& ) = delete;
};	

template <typename Type>
class Singleton : Noncopyable
{
public:
    static Type* getInstance()
    {
        pthread_once(&m_once, init);
        return m_pInstance;
    }

    static void init()
    {
        m_pInstance = new Type();
    }

private:
    Singleton();
    ~Singleton();

private:
    static Type* m_pInstance;
    static pthread_once_t m_once;
};

template<typename Type>
Type* Singleton<Type>::m_pInstance = nullptr;

template<typename Type>
pthread_once_t Singleton<Type>::m_once = PTHREAD_ONCE_INIT;


//demo------------------------------------
class Point
{
public:
    Point(){cout << "Point()" << endl;}
    ~Point(){cout << "~Point()"<< endl;}

    void init(int x, int y)
    {
        m_x = x;
        m_y = y;
        cout << "Point::init()" << endl;
    }

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
    Point* pt1 = Singleton<Point>::getInstance();
    Point* pt2 = Singleton<Point>::getInstance();
    pt1->init(1,2);
    pt2->init(2,4);

    cout << static_cast<Point*>(pt1) << endl;
    cout << static_cast<Point*>(pt2) << endl;
    cout << "*pt1 = " << *pt1 << endl;
    cout << "*pt2 = " << *pt2 << endl;

    return 0;
}
