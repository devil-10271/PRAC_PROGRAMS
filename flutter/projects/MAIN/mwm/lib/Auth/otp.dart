import 'package:demo/Auth/create_password.dart';
import 'package:flutter/material.dart';
import 'package:flutter_otp_text_field/flutter_otp_text_field.dart';

class otp extends StatefulWidget {
  const otp({super.key});

  @override
  State<otp> createState() => _otpState();
}

class _otpState extends State<otp> {
  @override
  Widget build(BuildContext context) {
    return SizedBox(
      width: 428,
      height: 436,
      child: Column(
        children: <Widget>[
          Padding(
            padding: const EdgeInsets.only(top: 30),
            child: Center(
              child: Text(
                'Enter OTP',
                style: TextStyle(
                  fontSize: 20,
                ),
              ),
            ),
          ),
          Container(
            margin: EdgeInsets.only(top: 20),
            width: 358,
            height: 40,
            child: RichText(
              textAlign: TextAlign.center,
              text: TextSpan(
                text:
                    'Please enter four digit code sent\nto your mobile number (480) 555-0121',
                style: TextStyle(
                  color: Colors.black,
                  fontSize: 16,
                ),
              ),
            ),
          ),
          Container(
            margin: EdgeInsets.only(top: 40),
            child: OtpTextField(
              numberOfFields: 4,
              borderColor: Color.fromRGBO(204, 204, 204, 1),
              fieldWidth: 54,
              fieldHeight: 54,
              borderRadius: BorderRadius.circular(10),
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,

              showFieldAsBox: true,
              onCodeChanged: (String code) {},

              // onSubmit: (String verificationCode){
              //   showDialog(
              //       context: context,
              //       builder: (context){
              //         return AlertDialog(
              //           title: Text("Verification Code"),
              //           content: Text('Code entered is $verificationCode'),
              //         );
              //       }
              //   );
              // }, // end onSubmit
            ),
          ),
          Padding(
            padding: const EdgeInsets.only(top: 20, left: 20),
            child: Align(
              alignment: Alignment.centerLeft,
              child: Row(
                children: [
                  RichText(
                    textAlign: TextAlign.left,
                    text: TextSpan(
                      text:
                          'Didn’t receive code?Resend                                   00:45',
                      style: TextStyle(
                        color: Colors.black,
                        fontSize: 16,
                      ),
                    ),
                  ),
                ],
              ),
            ),
          ),
          Padding(
            padding: const EdgeInsets.only(top: 70, left: 20, right: 20),
            child: Container(
              child: ElevatedButton(
                onPressed: () {
                  Navigator.push(context,
                      MaterialPageRoute(builder: (context) => create()));
                },
                style: ButtonStyle(
                  backgroundColor: MaterialStateProperty.all(
                      Color.fromRGBO(112, 43, 146, 1)),
                ),
                child: Center(
                  child: Text(
                    'Next',
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
    );
  }
}
