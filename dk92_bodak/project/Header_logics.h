#pragma once
#include <iostream>
#include <iomanip>
#include <Windows.h>
using namespace std;

float speed = 0, height = 0, compass = 0, horizon = 0, incline = 0;

void TimerFunction(int value)
{
    //A = A + 0.001;
    glutPostRedisplay();  // перерисовываем экран
    glutTimerFunc(33, TimerFunction, 1);  //запускаем таймер заново.
}

// генерация значений для моделирования
void DateAltimeter() {
    cout << "| " << setw(10) << speed/0.014   << 
          " Km | " << setw(10) << height*42857.1  <<
          " M | " << setw(10) << compass*720 << 
          " * | " << setw(10) << horizon*3.6 << 
          " * | " << setw(10) << incline*300 << " * |" << endl;
}

/*
 500
 0.7

*/
void DATE_speed() {
    float A = rand() % 500;
    if (A == 0) {
        A = 1;
    }
    A = A * 0.0014;
    while (A >= speed) {    
            speed += 0.001;
            Sleep(50);      
    }
    while (A <= speed) {
            speed -= 0.001;
            Sleep(50);    
    }
}

/*
30 000 
0.7

*/
void DATE_height() {
    float A = rand() % 30000;
    if (A == 0) {
        A = 1;
    }
    A = A * 0.000023;
    while (A >= height) {
        height += 0.001;
        Sleep(25);
    }
    while (A <= height) {
        height -= 0.001;
        Sleep(25);
    }
}

/*
360
1

*/
void DATE_compass() {
    float A = rand() % 360;
    if (A == 0) {
        A = 1;
    }
    A = A * 0.5;
    while (A >= compass) {
        compass += 0.01;
        Sleep(1);
    }
    while (A <= compass) {
        compass -= 0.01;
        Sleep(1);
    }
}

/*
 360

*/
void DATE_horizon() {
    //float A = rand() % 360 - 360;
    float A = rand() % 100 - 50;
    if (A == 0) {
        A = 1;
    }
    A = A / 3.6;
    while (A >= horizon) {
        horizon += 0.01;
        Sleep(1);
    }
    while (A <= horizon) {
        horizon -= 0.01;
        Sleep(1);
    }
}

/*
 90 - 90 


*/
void DATE_incline() {
    float A = rand() % 180 - 90;
    A = A / 300;
    while (A >= incline) {
        incline += 0.001;
        Sleep(10);
    }
    while (A <= incline) {
        incline -= 0.001;
        Sleep(10);
    }
}