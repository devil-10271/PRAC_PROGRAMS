import 'package:flutter/material.dart';

class Register extends StatefulWidget {
  const Register({super.key});

  @override
  State<Register> createState() => _RegisterState();
}

class _RegisterState extends State<Register> {

  bool _accepted=false;

  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 2,
      child: Scaffold(
        backgroundColor: Color.fromRGBO(112, 43, 146, 1),
        body: SingleChildScrollView(
          child: Stack(
            children: [
              Container(
                alignment: Alignment.topCenter,
                //padding: EdgeInsets.all(32),
                decoration: BoxDecoration(
                  image: DecorationImage(
                    image: AssetImage(
                        'assets/images/Train,_eat,_sleep,_poster_for_gym_with_fitness_icons,_vector-ai 1.png'),
                    fit: BoxFit.fitWidth,
                    alignment: Alignment.topCenter,
                  ),
                ),
                child: Column(
                  children: [
                    Container(
                      margin: EdgeInsets.only(top: 86),
                      width: 127,
                      height: 80,
                      decoration: BoxDecoration(
                        image: DecorationImage(
                          image: AssetImage(
                              'assets/images/MWM Logo - Colour-Hi-Res 2.png'),
                        ),
                      ),
                    ),
                    SizedBox(
                      height: 28,
                    ),
                    Container(
                      width: 233,
                      height: 50,
                      child: Center(
                        child: RichText(
                          textAlign: TextAlign.center,
                          text: TextSpan(
                            text: 'Register ',
                            style: TextStyle(
                                fontWeight: FontWeight.bold, fontSize: 20),
                            children: const <TextSpan>[
                              TextSpan(
                                  text: 'for Empowering',
                                  style:
                                      TextStyle(fontWeight: FontWeight.normal)),
                              TextSpan(
                                  text: ' \nYour Health Journey',
                                  style:
                                      TextStyle(fontWeight: FontWeight.normal)),
                            ],
                          ),
                        ),
                      ),
                    ),
                    Container(
                      margin: EdgeInsets.only(top: 48),
                      width: 428,
                      height: 633,
                      decoration: BoxDecoration(
                        color: Colors.white,
                        borderRadius: BorderRadius.only(
                            topRight: Radius.circular(45),
                            topLeft: Radius.circular(45)),
                      ),
                      child: Column(
                        children: [
                          SizedBox(
                            height: 25,
                          ),
                          Container(
                            margin: EdgeInsets.symmetric(horizontal: 20),
                            width: double.infinity,
                            height: 50,
                            decoration: BoxDecoration(
                              color: Color.fromRGBO(234, 234, 234, 1),
                              borderRadius:
                                  BorderRadius.all(Radius.circular(100)),
                            ),
                            child: TabBar(
                              //isScrollable: true,
                              tabAlignment: TabAlignment.fill,
                              indicatorColor: Colors.transparent,
                              dividerHeight: 0,
                              padding: EdgeInsets.symmetric(horizontal: 20),
                              unselectedLabelColor:
                                  Color.fromRGBO(74, 74, 74, 1),
                              labelColor: Color.fromRGBO(0, 0, 0, 1),
                              indicatorPadding:
                                  EdgeInsets.symmetric(vertical: 1),
                              indicator: BoxDecoration(
                                  color: Colors.white,
                                  borderRadius: BorderRadius.circular(100)),
                              tabs: [
                                Center(child: Tab(text: 'Sign in')),
                                Center(child: Tab(text: 'Register')),
                              ],
                            ),
                          ),
                          Expanded(
                            child: TabBarView(
                              children: [
                                // Content for Sign in tab
                                Padding(
                                  padding: const EdgeInsets.symmetric(
                                      vertical: 30, horizontal: 20),
                                  child: Column(
                                    //mainAxisAlignment: MainAxisAlignment.center,
                                    children: [
                                      TextField(
                                        //style: TextStyle(color: Colors.green),
                                        decoration: const InputDecoration(
                                          border: OutlineInputBorder(),
                                          label:
                                              Text('Enter your Email Address*'),
                                        ),
                                      ),
                                      SizedBox(
                                        height: 15,
                                      ),
                                      TextField(
                                        //style: TextStyle(color: Colors.green),
                                        decoration: const InputDecoration(
                                          border: OutlineInputBorder(),
                                          label: Text('Enter Password*'),
                                          suffixIcon: Image(
                                            image: AssetImage(
                                                'assets/icon/eye 1.png'),
                                          ),
                                        ),
                                      ),
                                      SizedBox(
                                        height: 12,
                                      ),
                                      Padding(
                                        padding:
                                            const EdgeInsets.only(left: 255),
                                        child: RichText(
                                          textAlign: TextAlign.right,
                                          text: TextSpan(
                                            text: 'Forgot Password?',
                                            style: TextStyle(
                                              color: Color.fromRGBO(
                                                  102, 102, 102, 1),
                                            ),
                                          ),
                                        ),
                                      ),
                                      Padding(
                                        padding: const EdgeInsets.symmetric(
                                            horizontal: 10, vertical: 40),
                                        child: Container(
                                          child: ElevatedButton(
                                            onPressed: null,
                                            style: ButtonStyle(
                                              backgroundColor:
                                                  MaterialStateProperty.all(
                                                      Color.fromRGBO(
                                                          112, 43, 146, 1)),
                                            ),
                                            child: Center(
                                              child: Text(
                                                'Sign in',
                                                style: TextStyle(
                                                  color: Colors.white,
                                                ),
                                              ),
                                            ),
                                          ),
                                        ),
                                      ),
                                      Row(
                                        children: [
                                          SizedBox(
                                            width: 60,
                                          ),
                                          Container(
                                            margin: EdgeInsets.all(10.0),
                                            color:
                                                Color.fromRGBO(74, 74, 74, 1),
                                            width: 60.0,
                                            height: 2.0,
                                          ),
                                          Text(
                                            'Or sign in with',
                                            style: TextStyle(
                                              color:
                                                  Color.fromRGBO(74, 74, 74, 1),
                                            ),
                                          ),
                                          Container(
                                            margin: EdgeInsets.all(10.0),
                                            color:
                                                Color.fromRGBO(74, 74, 74, 1),
                                            width: 60.0,
                                            height: 2.0,
                                          ),
                                        ],
                                      ),
                                      Padding(
                                        padding: const EdgeInsets.symmetric(
                                            horizontal: 25, vertical: 10),
                                        child: Row(
                                          children: [
                                            ElevatedButton(
                                              onPressed: null,
                                              style: ButtonStyle(
                                                backgroundColor:
                                                    MaterialStateProperty.all(
                                                        Color.fromRGBO(
                                                            234, 234, 234, 1)),
                                              ),
                                              child: Padding(
                                                padding:
                                                    const EdgeInsets.symmetric(
                                                        horizontal: 15,
                                                        vertical: 15),
                                                child: Image(
                                                    image: AssetImage(
                                                        'assets/icon/facebook.png')),
                                              ),
                                            ),
                                            SizedBox(
                                              width: 10,
                                            ),
                                            ElevatedButton(
                                              onPressed: null,
                                              style: ButtonStyle(
                                                backgroundColor:
                                                    MaterialStateProperty.all(
                                                        Color.fromRGBO(
                                                            234, 234, 234, 1)),
                                              ),
                                              child: Padding(
                                                padding:
                                                    const EdgeInsets.symmetric(
                                                        horizontal: 15,
                                                        vertical: 15),
                                                child: Image(
                                                    image: AssetImage(
                                                        'assets/icon/google.png')),
                                              ),
                                            ),
                                            SizedBox(
                                              width: 10,
                                            ),
                                            ElevatedButton(
                                              onPressed: null,
                                              style: ButtonStyle(
                                                backgroundColor:
                                                    MaterialStateProperty.all(
                                                        Color.fromRGBO(
                                                            234, 234, 234, 1)),
                                              ),
                                              child: Padding(
                                                padding:
                                                    const EdgeInsets.symmetric(
                                                        horizontal: 15,
                                                        vertical: 15),
                                                child: Image(
                                                    image: AssetImage(
                                                        'assets/icon/apple.png')),
                                              ),
                                            ),
                                          ],
                                        ),
                                      ),
                                      Padding(
                                        padding: const EdgeInsets.symmetric(vertical: 5,horizontal: 25),
                                        child: ElevatedButton(
                                          onPressed: null,
                                          style: ButtonStyle(
                                            backgroundColor:
                                                MaterialStateProperty.all(
                                                    Color.fromRGBO(
                                                        234, 234, 234, 1)),
                                          ),
                                          child: Center(
                                            child: Row(
                                              children: [
                                                Padding(
                                                  padding: const EdgeInsets.only(left: 110),
                                                  child: Row(
                                                    children: [
                                                      Padding(
                                                        padding: const EdgeInsets.symmetric( vertical: 15),
                                                        child: Image(
                                                            image: AssetImage('assets/icon/guest.png')
                                                        ),
                                                      ),
                                                      SizedBox(width: 10,),
                                                      Text(
                                                        'Guest',
                                                        style: TextStyle(
                                                          color: Colors.black,
                                                        ),
                                                      ),
                                                    ],
                                                  ),
                                                ),

                                              ],
                                            ),
                                          ),
                                        ),
                                      ),
                                    ],
                                  ),
                                ),
                                // Content for Register tab
                                Padding(
                                  padding: const EdgeInsets.symmetric(vertical: 30, horizontal: 20),
                                  child: Column(
                                    children: [
                                      TextField(
                                        //style: TextStyle(color: Colors.green),
                                        decoration: const InputDecoration(
                                          border: OutlineInputBorder(),
                                          label:
                                          Text('Enter First Name*'),
                                        ),
                                      ),
                                      SizedBox(height: 15,),
                                      TextField(
                                        //style: TextStyle(color: Colors.green),
                                        decoration: const InputDecoration(
                                          border: OutlineInputBorder(),
                                          label:
                                          Text('Enter Last Name*'),
                                        ),
                                      ),
                                      SizedBox(height: 15,),
                                      TextField(
                                        //style: TextStyle(color: Colors.green),
                                        decoration: const InputDecoration(
                                          border: OutlineInputBorder(),
                                          label:
                                          Text('Enter Email*'),
                                        ),
                                      ),
                                      SizedBox(height: 15,),
                                      TextField(
                                        //style: TextStyle(color: Colors.green),
                                        decoration: const InputDecoration(
                                          border: OutlineInputBorder(),
                                          label:
                                          Text('Enter Password*'),
                                          suffixIcon: Image(
                                            image: AssetImage(
                                                'assets/icon/eye-off 1.png'),
                                          ),
                                        ),
                                      ),
                                      SizedBox(height: 15,),
                                      TextField(
                                        //style: TextStyle(color: Colors.green),
                                        decoration: const InputDecoration(
                                          border: OutlineInputBorder(),
                                          label:
                                          Text('Confirm Password*'),
                                          suffixIcon: Image(
                                            image: AssetImage(
                                                'assets/icon/green_tick.png'),
                                          ),
                                        ),
                                      ),
                                      Row(
                                        children: [
                                          Checkbox(
                                            value: _accepted,
                                            onChanged: (newValue) {
                                              setState(() {
                                                _accepted = newValue!;
                                              });
                                            },
                                            side: BorderSide(color: Colors.black),
                                            activeColor: Color.fromRGBO(56, 165, 5, 1),
                                          ),
                                          Text('I accept the Terms and Conditions',
                                            style: TextStyle(
                                              color: Colors.black,
                                              fontSize: 12,
                                            ),
                                          ),
                                        ],
                                      ),
                                      Padding(
                                        padding: const EdgeInsets.symmetric(
                                            horizontal: 10, vertical: 10),
                                        child: Container(
                                          child: ElevatedButton(
                                            onPressed: null,
                                            style: ButtonStyle(
                                              backgroundColor:
                                              MaterialStateProperty.all(
                                                  Color.fromRGBO(
                                                      112, 43, 146, 1)),
                                            ),
                                            child: Center(
                                              child: Text(
                                                'REGISTER ACCOUNT',
                                                style: TextStyle(
                                                  color: Colors.white,
                                                ),
                                              ),
                                            ),
                                          ),
                                        ),
                                      ),
                                    ],
                                  ),
                                ),
                              ],
                            ),
                          ),
                        ],
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
