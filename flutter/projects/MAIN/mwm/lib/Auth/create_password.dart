import 'package:demo/Auth/Register.dart';
import 'package:flutter/material.dart';

class create extends StatefulWidget {
  const create({super.key});

  @override
  State<create> createState() => _createState();
}

class _createState extends State<create> {
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
                            text: 'Create New Password',
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
                            margin: EdgeInsets.only(top: 38),
                            width: 140,
                            height: 140,
                            decoration: BoxDecoration(
                              image: DecorationImage(
                                image: AssetImage(
                                    'assets/images/create_password.png'),
                                alignment: Alignment.center,
                              ),
                            ),
                          ),
                          Container(
                            margin: EdgeInsets.only(top: 38),
                            width: 358,
                            height: 40,
                            child: RichText(
                              textAlign: TextAlign.center,
                              text: TextSpan(
                                text:
                                    'Your new password must be different from that\nof previously used passwords.',
                                style: TextStyle(
                                  color: Colors.black,
                                ),
                              ),
                            ),
                          ),
                          Container(
                            margin:
                                EdgeInsets.only(top: 30, left: 20, right: 20),
                            child: Column(
                              children: [
                                TextField(
                                  //style: TextStyle(color: Colors.green),
                                  decoration: const InputDecoration(
                                    border: OutlineInputBorder(),
                                    label: Text('Enter Password*'),
                                    suffixIcon: Image(
                                      image: AssetImage(
                                          'assets/icon/eye-off 1.png'),
                                    ),
                                  ),
                                ),
                                SizedBox(
                                  height: 15,
                                ),
                                TextField(
                                  //style: TextStyle(color: Colors.green),
                                  decoration: const InputDecoration(
                                    border: OutlineInputBorder(),
                                    label: Text('Confirm Password*'),
                                    suffixIcon: Image(
                                      image: AssetImage(
                                          'assets/icon/green_tick.png'),
                                    ),
                                  ),
                                ),
                              ],
                            ),
                          ),
                          Padding(
                            padding: const EdgeInsets.symmetric(
                                horizontal: 10, vertical: 50),
                            child: Container(
                              child: ElevatedButton(
                                onPressed: () {
                                  Navigator.push(
                                      context,
                                      MaterialPageRoute(
                                          builder: (context) => Register()
                                      )
                                  );
                                },
                                style: ButtonStyle(
                                  backgroundColor: MaterialStateProperty.all(
                                      Color.fromRGBO(112, 43, 146, 1)),
                                ),
                                child: Center(
                                  child: Text(
                                    'SUBMIT',
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
