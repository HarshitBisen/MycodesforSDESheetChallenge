bool issafe(int v[9][9],int r,int c,int n)

{

   for(int i=0;i<9;i++)

   {

       if(v[r][i]==n)

           return false;

   }

   for(int i=0;i<9;i++)

   {

       if(v[i][c]==n)

           return false;

   }

   int st=r-r%3,co=c-c%3;

   for(int i=0;i<3;i++)

   {

       for(int j=0;j<3;j++)

       {

           if(v[i+st][j+co]==n)

               return false;

       }

   }

   return true;

}

bool solve(int v[9][9],int r,int c)

{

   if(r==8 && c==9)

       return true;

   if(c==9)

   {

       r++;

       c=0;

   }

   if(v[r][c]>0)

       return solve(v,r,c+1);

   for(int i=1;i<=9;i++)

   {

       if(issafe(v,r,c,i))

       {

           v[r][c]=i;

           if(solve(v,r,c+1))

               return true;

       }

       v[r][c]=0;        

   }

   return false;

}

bool isItSudoku(int matrix[9][9]) {

   if(solve(matrix,0,0))

       return true;

   return false;

}
