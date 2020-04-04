#include <iostream>
#include <stdlib.h> //使用函数atexit
#include <pthread.h> //使用线程函数
using namespace std;

// 单例模式2：atexit + pthread_once
// ps：只能在Linux环境下，因为关联了POSIX的线程库

// 单例类
class Singleton
{
public:
    // 获取对象
    // 在多线程下是非线程安全的，如果想要线程安全，则需要加锁
    static Singleton* getInstance()
    {
        pthread_once(&m_once, init);
        return m_pInstance;
    }

    static void init()
    {
        m_pInstance = new Singleton();
        atexit(destory);
    }

    static void destory()
    {
        if(m_pInstance != nullptr)
        {
            delete m_pInstance;
        }
    }

private:
    Singleton() {cout << "Singleton()" << endl;}
    ~Singleton() {cout << "~Singleton()" << endl;}
    static Singleton* m_pInstance;
    static pthread_once_t m_once;
};

// 当用到单例模式时，对象才初始化，称之为饿汉模式(懒汉模式，懒加载)。优点：节省空间，缺点：需要加锁，浪费效率。
Singleton* Singleton::m_pInstance = nullptr;
pthread_once_t Singleton::m_once = PTHREAD_ONCE_INIT;

// 在进入main函数之前就创建在堆空间里面，所以是线程安全的，又称饱汉模式。优点：节省效率，缺点：浪费堆空间。
/* Singleton* Singleton::m_pInstance = getInstance(); */

int main()
{
    Singleton* p1 = Singleton::getInstance();
    Singleton* p2 = Singleton::getInstance();
    cout << "p1 = " << p1 << endl;
    cout << "p2 = " << p2 << endl;
    return 0;
}

