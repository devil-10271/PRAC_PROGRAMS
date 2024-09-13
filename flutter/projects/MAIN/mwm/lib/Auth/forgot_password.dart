import 'package:demo/Auth/create_password.dart';
import 'package:demo/Auth/otp.dart';
import 'package:flutter/material.dart';
import 'package:flutter_otp_text_field/flutter_otp_text_field.dart';

class forgot extends StatefulWidget {
  const forgot({super.key});

  @override
  State<forgot> createState() => _forgotState();
}

class _forgotState extends State<forgot> {
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
                          alignment: Alignment.center,
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
                            text: 'Forgot Password ',
                            style: TextStyle(
                                fontWeight: FontWeight.bold, fontSize: 20),
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
                          Container(
                            margin: EdgeInsets.only(top: 45),
                            width: 170,
                            height: 160,
                            decoration: BoxDecoration(
                              image: DecorationImage(
                                image: AssetImage('assets/images/lock.png'),
                                alignment: Alignment.center,
                              ),
                            ),
                          ),
                          Container(
                            margin: EdgeInsets.only(top: 50),
                            width: 358,
                            height: 60,
                            child: RichText(
                              textAlign: TextAlign.center,
                              text: TextSpan(
                                text:
                                    'Enter the email associated with your account '
                                    '\nand we’ll send an email with instructions to '
                                    '\nreset your password.',
                                style: TextStyle(
                                  color: Colors.black,
                                  fontSize: 16
                                ),
                              ),
                            ),
                          ),
                          Padding(
                            padding: const EdgeInsets.only(top: 30,right: 15,left: 15),
                            child: TextField(
                              //style: TextStyle(color: Colors.green),
                              decoration: const InputDecoration(
                                border: OutlineInputBorder(),
                                label:
                                Text('Enter Email*'),
                              ),
                            ),
                          ),
                          Padding(
                            padding: const EdgeInsets.only(top: 70,left: 20,right: 20),
                            child: Container(
                              child: ElevatedButton(
                                onPressed: () {
                                    showModalBottomSheet<void>(
                                      context: context,
                                      builder: (context) => otp(),
                                    );
                                },
                                style: ButtonStyle(
                                  backgroundColor:
                                  MaterialStateProperty.all(
                                      Color.fromRGBO(
                                          112, 43, 146, 1)),
                                ),
                                child: Center(
                                  child: Text(
                                    'GET OTP',
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
      ),
    );
  }
}
