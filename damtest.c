#include<stdio.h>
#include<math.h>
#define _USE_MATH_DEFINES
void main()
{
  float G=9.811;
  float P,A,r,h,d,x,y,T,P1,P2,P3,j,m;
  printf("Enter the radius and height of the free surface\n from the gate:");
  scanf("%f%f",&r,&h);
  printf("Enter the percentage of closed gate\n");
  scanf("%f",&y);
  d=r+r;
  do {
    j=y/100;
    m=j*0.08;
    if(m<=0.5)
    {
      x=(m*d)-(j*d);
      A=acos(x*(d/r));
    }
    else
    {
      x = (j*d)-(m*d);
      T=acos((x*d)/r);
      A=((360-(2*T))/2);
      break;
    }
    A=A*M_PI/180;
    P1=(G*r*r);
    P2=(h+r)*(A-((sin(A))*(cos(A))));
    P3=((2/3)*r*pow(sin(A),3));
    P=P1*(P2-P3);
    y=y++;
    printf("Pressure Force Acting on the gate=%f",P);
  } while(y<=100);
}
