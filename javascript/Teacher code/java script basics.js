<html>
    <head>
       <title>JS</title>
       <script type="text/javascript" src="message.js"></script>
    </head>
    <body>
        <p>welcome</p>
        <script type="text/javascript">

              <!-----------conditional statements----------->
            let a = 20;
            if(a == 10)
            {
                document.write(" a is 10");
            }
            else if(a == 15)
            {
                document.write(" a is 15");
            }
            else if(a == 21)
            {
                document.write(" a is 20");
            }
            else{
                document.write(" a is not 10,15,20");
            }*/
            //for loop example
            for(i=0;i<5;i++)
            {
                document.write("<br> The value of i is " + i);
            }
            i1=0;
            while(i1<5)
            {
                document.write("<br> hello");
                i1++;
            }


            //Switch statement
            var grade="B1";
            var result;
            switch(grade)
            {
                case 'A':
                result = "A Grade";
                document.write(result);
                break;
                case 'B':
                result = "B Grade";
                document.write(result);
                break;
                case 'C':
                result = "C Grade";
                document.write(result);
                break;
                default:
                result="no grade";
                document.write(result);
            }


            // function
            function message()
            {
                document.writeln(" <br> hello  I am from function");
            }
            message();

            //function with arguments
            function square(a,b,c)
            {
                document.write("<br>" + a*b*c);
            }
            square(2,3,4);

            function info()
            {
                square(2,3,4);
                return "Hello how are you?"
            }
            var info_val = info();
            document.write("<br>" + info());


            //Arrays
            var fruits = ["banana","apple","pear"];
            for(i=0;i<fruits.length;i++)
            {
                document.write("<br>" + fruits[i]);
            }

            var cars = new Array();
            cars[0] = "bmw";
            cars[1] = "Mustang black";
            var emp = new Array("xyz","abc","hjh");

            // methods of Array
            /*concat()
            pop()
            push()
            length()*/

            //var arr_result = ;
            document.writeln("<br>" + cars.concat(emp));
            document.writeln("<br>" + cars.push("Volvo"));
            document.writeln("<br>" + cars);


            // string 
            var stringname = "Hello";
            var sname = new String("Hello are you here");

            // String methods
           /*concat();
            search();
            replace();
            toLowerCase(); */
            document.write("<br>" + stringname.toLowerCase());

            // Date 
            /*Date()
            Date(milliseconds)
            Date(dateString)
            Date(year,month,day,hours,minutes,seconds,milliseconds)
            
            //methods
            getDate()
            getDay() 
            getFullYears()
            getHours()
            getMilliseconds()*/
            var today = new Date();
            document.write(today);
        </script>
    </body>
</html>
