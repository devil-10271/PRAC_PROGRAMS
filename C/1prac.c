// for multi dimentianal array


#include "stdio.h"
#include "conio.h"
// #include"iostream"

int main()
{
    int i = 0, j = 0;
    int row, col;
    printf("Enter the Rows : ");
    scanf("%d", &row);
    printf("Enter the Columns : ");
    scanf("%d", &col);

    int a[row][col];
    for (i = 0; i < row; i++)
    {
        for (j = 0; j < col; j++)
        {
            printf("arr [%d][%d] : ", i, j);
            scanf("%d", &a[i][j]);
        }
        printf("\n");
    }
    printf("\n\n");

    for (i = 0; i < row; i++)
    {
        for (j = 0; j < col; j++)
        {
            printf("arr [%d][%d] : %d  ", i, j,a[i][j] );
        }
        printf("\n");
    }

    return 0;
}