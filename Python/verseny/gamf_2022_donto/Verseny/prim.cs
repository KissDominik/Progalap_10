using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace primszam
{
    class Program
    {
        static void Main(string[] args)
        {

            int n = 1000000;
            Hany_db(n);
            Console.ReadKey();

        }

        static int Fact(int n)
        {
            int i, fact = 1, number;
            number = n;
            for (i = 1; i <= number; i++)
            {
                fact = fact * i;
            }
            return fact;
        }

        static double PrimE(int n)
        {
            double szam = 0;
            szam = Fact(n - 1);
            szam += 1;
            szam /= n;
            szam *= Math.PI;
            szam = Math.Cos(szam);
            szam *= szam;
            szam = Math.Floor(szam);               
            return szam;
        }
        static void Hany_db(int eddig)
        {
            int db = 0;
            for(int i = 0;i<eddig+1;i++)
            {
                Console.WriteLine(i);
                if (PrimE(i) == 1)
                {
                    db++;
                }
                    
            }
            Console.WriteLine(db);
        }

    }
}