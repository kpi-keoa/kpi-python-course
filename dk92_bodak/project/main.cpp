#include <iostream>
#include <iomanip>
#include "Header_graphics.h"
#include "Header_logics.h"
#include "GL/freeglut.h"
#include <thread>
#include <Windows.h>
using namespace std;

// функция рендеренга
void renderScene(void) {
    //Logic_fun();
    Display();
}


int main(int argc, char** argv)
{
    system("color a");
    cout << "| " << setw(10) << "speed" <<
        " Km | " << setw(10) << "height" <<
        " M | " << setw(10) << "compass" <<
        " * | " << setw(10) << "horizon" <<
        " * | " << setw(10) << "incline" << "  |" << endl;
    // дополнительные потоки для обновления даных моделирования
    thread p_speed([] {
        while (true) {
            Logic_fun(); 
            DATE_speed();
        } });
    p_speed.detach();
   
    thread p_height([] {
        while (true) {
            //Logic_fun(); 
            DATE_height();
        } });
    p_height.detach();
    
    thread p_compass([] {
        while (true) {
            Logic_fun(); 
            DATE_compass();
        } });
    p_compass.detach();
    
    thread p_horizon([] {
        while (true) {
            Logic_fun(); 
            DATE_horizon();
        } });
    p_horizon.detach();
    
    thread p_incline([] {
        while (true) {
            Logic_fun(); 
            DATE_incline();
        } });
    p_incline.detach();
    
    // инициализация
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA);
    glutInitWindowPosition(400, 0);
    glutInitWindowSize(800,800);

    glutCreateWindow("Altimeter");
    glClearColor(1.0f, 0.5f, 0.0f, 0.0f);
    glClear(GL_COLOR_BUFFER_BIT);
    glutDisplayFunc(renderScene);

    //glutCreateWindow("Altimeter1");
    //glClearColor(0.9f, 0.1f, 0.1f, 1.0f);
    //glClear(GL_COLOR_BUFFER_BIT);
    //glutDisplayFunc(renderScene);

    glutTimerFunc(33, TimerFunction, 1);
    glutMainLoop();




    return 0;
}