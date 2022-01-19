#pragma once
#include <iostream>
#include <iomanip>
#include "GL/freeglut.h"
#include "Header_logics.h.h"
#include <cmath>

#include <Windows.h>

using namespace std;
/*
                Значение mode	Описание
    GL_POINTS	        Каждый вызов glVertex задает отдельную точку.
    GL_LINES	        Каждая пара вершин задает отрезок.
    GL_LINE_STRIP	    Рисуется ломанная.
    GL_LINE_LOOP	    Рисуется ломанная, причем ее последняя точка соединяется с первой.
    GL_TRIANGLES	    Каждые три вызова glVertex задают треугольник.
    GL_TRIANGLE_STRIP	Рисуются треугольники с общей стороной.
    GL_TRIANGLE_FAN	    Тоже самое, но по другому правилу соединяются вершины, вряд ли понадобится.
    GL_QUADS	        Каждые четыре вызова glVertex задают четырехугольник.
    GL_QUAD_STRIP	    Четырехугольники с общей стороной.
    GL_POLYGON	        Многоугольник.
*/
/*
                                  Y
                                /\
                                |
                                |
                                |
                       ------------------->
                       -X       |           X
                                |
                                |
                                 -Y

*/
//--------------------------------------------------------
int color_mode = 0;
int icon_mode = 1;

//--------------------------------------------------------

void Gorizont_icon() {

    if (icon_mode == 0) {
        glColor4d(1, 1, 0, 0.9);
        glPointSize(6);
        glBegin(GL_POINTS);
        glVertex2f(0, 0.5);
        glEnd();
        glLineWidth(6);
        glBegin(GL_LINES);
        glVertex2f(-0.3, 0.5);
        glVertex2f(-0.1, 0.5);
        glVertex2f(0.1, 0.5);
        glVertex2f(0.3, 0.5);
        glEnd();
        glLineWidth(2);
    }
    else if (icon_mode == 1) {
        glColor4d(1, 1, 0, 0.9);
        glBegin(GL_POLYGON);
        glVertex2f(0, 0.5);
        glVertex2f(-0.2, 0.4);
        glVertex2f(-0.3, 0.4);
        glVertex2f(0, 0.5);
        glVertex2f(0.2, 0.4);
        glVertex2f(0.3, 0.4);
        glVertex2f(0, 0.5);
        glEnd();

        glColor4d(0.6, 0.6, 0, 0.9);
        glBegin(GL_POLYGON);
        glVertex2f(0, 0.5);
        glVertex2f(-0.1, 0.4);
        glVertex2f(-0.2, 0.4);
        glVertex2f(0, 0.5);
        glVertex2f(0.1, 0.4);
        glVertex2f(0.2, 0.4);
        glVertex2f(0, 0.5);
        glEnd();

        glColor4d(1, 1, 0, 0.9);
        glLineWidth(6);
        glBegin(GL_LINES);
        glVertex2f(-0.4, 0.5);
        glVertex2f(-0.2, 0.5);
        glVertex2f(0.2, 0.5);
        glVertex2f(0.4, 0.5);
        glEnd();
        glLineWidth(2);
    }

    //glBegin(GL_LINE_LOOP);
    //glVertex2f(-0.05, 0.5);
    //glVertex2f(0, 0.45);
    //glVertex2f(0.05, 0.5);
    //glEnd();
    
}


// табло наклона
void Shkala_naklon() {

    glColor3d(1, 1, 1);
    glBegin(GL_LINES);
    glVertex2f(-0.05, incline + 0.55);
    glVertex2f(0.05, incline + 0.55);
    glVertex2f(-0.1, incline + 0.6);
    glVertex2f(0.1, incline + 0.6);
    glVertex2f(-0.05, incline + 0.65);
    glVertex2f(0.05, incline + 0.65);
    glVertex2f(-0.15, incline + 0.7);
    glVertex2f(0.15, incline + 0.7);
    glVertex2f(-0.05, incline + 0.75);
    glVertex2f(0.05, incline + 0.75);
    glVertex2f(-0.1, incline + 0.8);
    glVertex2f(0.1, incline + 0.8);
    //+++++++++++++++++++++++
    glVertex2f(-0.05, incline + 0.45);
    glVertex2f(0.05, incline + 0.45);
    glVertex2f(-0.1, incline + 0.4);
    glVertex2f(0.1, incline + 0.4);
    glVertex2f(-0.05, incline + 0.35);
    glVertex2f(0.05, incline + 0.35);
    glVertex2f(-0.15, incline + 0.3);
    glVertex2f(0.15, incline + 0.3);
    glVertex2f(-0.05, incline + 0.25);
    glVertex2f(0.05, incline + 0.25);
    glVertex2f(-0.1, incline + 0.2);
    glVertex2f(0.1, incline + 0.2);
    glEnd();

}

void Ramka_datchicov() {

    glColor3d(0, 0, 0);
    glBegin(GL_QUADS);
    glVertex2f(-0.6, 1);
    glVertex2f(-0.6, 0.9);
    glVertex2f(-0.4, 0.9);
    glVertex2f(-0.3, 1);

    glVertex2f(0.6, 1);
    glVertex2f(0.6, 0.9);
    glVertex2f(0.4, 0.9);
    glVertex2f(0.3, 1);

    glVertex2f(-0.6, 0);
    glVertex2f(-0.4, 0);
    glVertex2f(-0.2, -0.2);
    glVertex2f(-0.6, -0.2);

    glVertex2f(0.6, 0);
    glVertex2f(0.4, 0);
    glVertex2f(0.2, -0.2);
    glVertex2f(0.6, -0.2);

    glEnd();


    // Рамка 
    glColor3d(1, 1, 1);
    glBegin(GL_LINE_LOOP);
    glVertex2f(-0.3, 0.999);
    glVertex2f(-0.4, 0.9);
    glVertex2f(-0.4, 0);
    glVertex2f(-0.3, -0.1);
    glVertex2f(0.3, -0.1);
    glVertex2f(0.4, 0);
    glVertex2f(0.4, 0.9);
    glVertex2f(0.3, 0.999);
    glEnd();
    glBegin(GL_LINES);
    glVertex2f(-0.4, 0.9);
    glVertex2f(-1, 0.9);
    glVertex2f(-1, 0);
    glVertex2f(-0.4, 0);
    glVertex2f(0.4, 0.9);
    glVertex2f(1, 0.9);
    glVertex2f(1, 0);
    glVertex2f(0.4, 0);
    glEnd();
    /*
    glColor3d(1, 1, 1);
    glBegin(GL_LINE_LOOP);
    for (int ii = 0; ii < 100; ii++)
    {
        if (ii <= 50) {

        
        float theta = 2.0f * 3.1415926f * float(ii) / float(100);
        float x = 0.35 * cosf(theta);
        float y = 0.35 * sinf(theta);
        glVertex2f(x + 0, y + 0.5);
        }
    }
    glEnd();
    */
}


void Horizon() {

    float theta = 0;
    float x = 0;
    float y = 0;
    glColor3d(0, 0.7, 1);
    glBegin(GL_POLYGON);
    theta = 2.0f * 3.1415926f * float(0 + horizon) / float(100);
    x = 1.5 * cosf(theta);
    y = 1.5 * sinf(theta);
    glVertex2f(x + 0, y + 0.5);
    theta = 2.0f * 3.1415926f * float(25 + horizon) / float(100);
    x = 1.5 * cosf(theta);
    y = 1.5 * sinf(theta);
    glVertex2f(x + 0, y + 0.5);
    theta = 2.0f * 3.1415926f * float(50 + horizon) / float(100);
    x = 1.5 * cosf(theta);
    y = 1.5 * sinf(theta);
    glVertex2f(x + 0, y + 0.5);
    glEnd();

    glColor3d(0, 0, 0);
    glBegin(GL_LINE_LOOP);
    theta = 2.0f * 3.1415926f * float(25 + horizon) / float(100);
    x = 1.5 * cosf(theta);
    y = 1.5 * sinf(theta);
    glVertex2f(x + 0, y + 0.5);
    theta = 2.0f * 3.1415926f * float(0 + horizon) / float(100);
    x = 1.5 * cosf(theta);
    y = 1.5 * sinf(theta);
    glVertex2f(x + 0, y + 0.5);
    theta = 2.0f * 3.1415926f * float(50 + horizon) / float(100);
    x = 1.5 * cosf(theta);
    y = 1.5 * sinf(theta);
    glVertex2f(x + 0, y + 0.5);
    glEnd();

    // TANGASH
    /*
    glColor3d(1, 1, 1);
    glBegin(GL_LINE_LOOP);
    for (int ii = 0; ii < 100; ii++)
    {
        float theta = 2.0f * 3.1415926f * float(ii) / float(100);
        float x = 0.4 * cosf(theta);
        float y = 0.4 * sinf(theta);
        glVertex2f(x + 0, y + 0.5);
    }
    glEnd();
    */

  
}


void Fon() {
    glColor3d(1, 1, 1);
    glBegin(GL_POLYGON);
    glVertex2f(-0.6, 1);
    glVertex2f(-1, 1);
    glVertex2f(-1, -1);
    glVertex2f(-0.6, -1);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex2f(1, 1);
    glVertex2f(0.6, 1);
    glVertex2f(0.6, -1);
    glVertex2f(1, -1);
    glEnd();
}


void Details() {
    // Самолёт
    glColor3d(1, 1, 1);
    glBegin(GL_LINE_LOOP);
    glVertex2f(0, -0.35);
    glVertex2f(0.01, -0.4);
    glVertex2f(0.03, -0.4);
    glVertex2f(0.04, -0.5);
    glVertex2f(0.3, -0.5);
    glVertex2f(0.3, -0.56);
    glVertex2f(0.04, -0.59);
    glVertex2f(0.03, -0.75);
    glVertex2f(0.2, -0.75);
    glVertex2f(0.2, -0.8);
    glVertex2f(0.04, -0.8);
    glVertex2f(0.01, -0.78);
    glVertex2f(0.01, -0.85);
    glVertex2f(0, -0.85);
    glVertex2f(-0, -0.85);
    glVertex2f(-0.01, -0.85);
    glVertex2f(-0.01, -0.78);
    glVertex2f(-0.04, -0.8);
    glVertex2f(-0.2, -0.8);
    glVertex2f(-0.2, -0.75);
    glVertex2f(-0.03, -0.75);
    glVertex2f(-0.04, -0.59);
    glVertex2f(-0.3, -0.56);
    glVertex2f(-0.3, -0.5);
    glVertex2f(-0.04, -0.5);
    glVertex2f(-0.03, -0.4);
    glVertex2f(-0.01, -0.4);
    glVertex2f(-0, -0.35);
    glEnd();

}

void Ukazatel_krena() {

    glColor4d(1, 0, 0, 0.8);
    glBegin(GL_POLYGON);
    glVertex2f(0, 0);
    glVertex2f(0.05, -0.18);
    glVertex2f(-0.05, -0.18);
    glEnd();

}


void Compas() {
    // фон
    glColor3d(0.1, 0.1, 0.1);
    glBegin(GL_POLYGON);
    for (int ii = 0; ii < 100; ii++)
    {
        float theta = 2.0f * 3.1415926f * float(ii) / float(100);
        float x = 1 * cosf(theta);
        float y = 1 * sinf(theta);
        glVertex2f(x + 0, y + -1);

    }
    glEnd();
    glColor3d(1, 1, 1);
    // большая линия
    glBegin(GL_LINE_LOOP);
    for (int ii = 0; ii < 100; ii++)
    {
        float theta = 2.0f * 3.1415926f * float(ii) / float(100);
        float x = 1 * cosf(theta);
        float y = 1 * sinf(theta);
        glVertex2f(x + 0, y + -1);
    }
    glEnd();
    // маленькая линия
    glBegin(GL_LINE_LOOP);
    for (int ii = 0; ii < 100; ii++)
    {
        float theta = 2.0f * 3.1415926f * float(ii) / float(100);
        float x = 0.85 * cosf(theta);
        float y = 0.85 * sinf(theta);
        glVertex2f(x + 0, y + -1);
    }
    glEnd();
    // шкала
    glBegin(GL_LINES);
    for (int ii = 0; ii < 180; ii++)
    {
        glColor3d(1, 1, 1);
        if (ii == 45) {
            glColor3d(1, 0, 0);
        }
        else if (ii == 135) {
            glColor3d(0, 0, 1);
        }
        float theta = 2.0f * 3.1415926f * float(ii + compass) / float(180);
        float x = 0.85 * cosf(theta);
        float y = 0.85 * sinf(theta);
       
        glVertex2f(0 + x, -1 + y);
        if (ii % 2) {
            x = 0.93 * cosf(theta);
            y = 0.93 * sinf(theta);
            glVertex2f(x + 0, y + -1);
        }
        else {
            x = 0.88 * cosf(theta);
            y = 0.88 * sinf(theta);
            glVertex2f(x + 0, y + -1);
        }
         
    }
    glEnd();
}
//--------------------------------------------------------

void Vertical_Speed() {
    glColor3d(1, 1, 1);
    glBegin(GL_LINE_LOOP);
        glVertex2f(0.3, 0.8);
        glVertex2f(0.4, 0.8);
        glVertex2f(0.4, 0.1);
        glVertex2f(0.3, 0.1);
    glEnd();

    glBegin(GL_LINES);
        glVertex2f(0.35, 0.7);
        glVertex2f(0.4, 0.7);
        glVertex2f(0.35, 0.6);
        glVertex2f(0.4, 0.6);
        glVertex2f(0.35, 0.5);
        glVertex2f(0.4, 0.5);
        glVertex2f(0.35, 0.4);
        glVertex2f(0.4, 0.4);
        glVertex2f(0.35, 0.3);
        glVertex2f(0.4, 0.3);
        glVertex2f(0.35, 0.2);
        glVertex2f(0.4, 0.2);

        glVertex2f(0.35, 0.75);
        glVertex2f(0.4, 0.75);
        glVertex2f(0.35, 0.65);
        glVertex2f(0.4, 0.65);
        glVertex2f(0.35, 0.55);
        glVertex2f(0.4, 0.55);
        glVertex2f(0.35, 0.45);
        glVertex2f(0.4, 0.45);
        glVertex2f(0.35, 0.35);
        glVertex2f(0.4, 0.35);
        glVertex2f(0.35, 0.25);
        glVertex2f(0.4, 0.25);
        glVertex2f(0.35, 0.15);
        glVertex2f(0.4, 0.15);
    glEnd();

}


void Menu() {
    glColor3d(0.3, 0.3, 0.3);
    glBegin(GL_QUADS);
    glVertex2f(-0.6, 1);
    glVertex2f(-0.6, -1);
    glVertex2f(0.6, -1);
    glVertex2f(0.6, 1);

    glEnd();

}

void Hanging_Indicator() {
    glColor3d(1, 1, 1);
    glBegin(GL_LINES);
    glVertex2f(0.6, 0.8);
    glVertex2f(0.5, 0.8);
    glVertex2f(0.6, 0.7);
    glVertex2f(0.5, 0.7);
    glVertex2f(0.6, 0.6);
    glVertex2f(0.5, 0.6);
    glVertex2f(0.6, 0.5);
    glVertex2f(0.5, 0.5);
    glVertex2f(0.6, 0.4);
    glVertex2f(0.5, 0.4);
    glVertex2f(0.6, 0.3);
    glVertex2f(0.5, 0.3);
    glVertex2f(0.6, 0.2);
    glVertex2f(0.5, 0.2);
    glVertex2f(0.6, 0.1);
    glVertex2f(0.5, 0.1);

    glEnd();

    //+++++++++++++++++++++++++++++++++++++++++++
    glColor3d(0.1, 0.1, 0.1);
    glBegin(GL_POLYGON);
    glVertex2f(0.6, 0.1 + height);
    glVertex2f(0.55, 0.15 + height);
    glVertex2f(0.41, 0.15 + height);
    glVertex2f(0.41, 0.05 + height);
    glVertex2f(0.55, 0.05 + height);
    glEnd();

    glColor3d(1, 1, 1);
    glBegin(GL_LINE_LOOP);
    glVertex2f(0.6, 0.1 + height);
    glVertex2f(0.55, 0.15 + height);
    glVertex2f(0.41, 0.15 + height);
    glVertex2f(0.41, 0.05 + height);
    glVertex2f(0.55, 0.05 + height);
    glEnd();

}



void Speed_Indicator() {

    glColor3d(1, 1, 1);
    glBegin(GL_LINES);
    glVertex2f(-0.6, 0.8);
    glVertex2f(-0.5, 0.8);
    glVertex2f(-0.6, 0.7);
    glVertex2f(-0.5, 0.7);
    glVertex2f(-0.6, 0.6);
    glVertex2f(-0.5, 0.6);
    glVertex2f(-0.6, 0.5);
    glVertex2f(-0.5, 0.5);
    glVertex2f(-0.6, 0.4);
    glVertex2f(-0.5, 0.4);
    glVertex2f(-0.6, 0.3);
    glVertex2f(-0.5, 0.3);
    glVertex2f(-0.6, 0.2);
    glVertex2f(-0.5, 0.2);
    glVertex2f(-0.6, 0.1);
    glVertex2f(-0.5, 0.1);

    glEnd();

    // Шкала
    glLineWidth(9);
    glColor3d(1, 1, 1);
    glBegin(GL_LINES);
    
    glVertex2f(-0.58, 0.9);
    glVertex2f(-0.58, 0.1);

    glColor3d(1, 0, 0);
    glVertex2f(-0.59, 0.9);
    glVertex2f(-0.59, 0.1);

    glColor3d(1, 1, 0);
    glVertex2f(-0.59, 0.7);
    glVertex2f(-0.59, 0.1);

    glColor3d(0, 1, 0);
    glVertex2f(-0.59, 0.3);
    glVertex2f(-0.59, 0.1);

    glEnd();

    glLineWidth(2);


    //+++++++++++++++++++++++++++++++++++++++++++
    glColor3d(0.1, 0.1, 0.1);
    glBegin(GL_POLYGON);
    glVertex2f(-0.6, 0.1 + speed);
    glVertex2f(-0.55, 0.15 + speed);
    glVertex2f(-0.41, 0.15 + speed);
    glVertex2f(-0.41, 0.05 + speed);
    glVertex2f(-0.55, 0.05 + speed);
    glEnd();

    glColor3d(1, 1, 1);
    glBegin(GL_LINE_LOOP);
    glVertex2f(-0.6, 0.1 + speed);
    glVertex2f(-0.55, 0.15 + speed);
    glVertex2f(-0.41, 0.15 + speed);
    glVertex2f(-0.41, 0.05 + speed);
    glVertex2f(-0.55, 0.05 + speed);
    glEnd();
}


void Tekst() {

}


// функция логики
void Logic_fun() {
    DateAltimeter();
}

// галва функция для отрисовки всех елементов
void Display() {

    glClearColor(0.9, 0.6, 0, 0);
    glEnable(GL_BLEND);
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    // Тело графики

    Horizon();
    Speed_Indicator();
    Hanging_Indicator();
    Ramka_datchicov();
    Vertical_Speed();
    Shkala_naklon();
    Compas();
    Details();
    Gorizont_icon();
    Ukazatel_krena();
    //Всегда последние
    Fon();
    Tekst();
    // Инженерное меню

    //Menu();

    glutSwapBuffers();
}