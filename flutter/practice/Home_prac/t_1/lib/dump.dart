Map Dump = {
  'Day 1 2 3': Container(
    color: Colors.pink,
    // width: MediaQuery.of(context).size.width * 0.5,
    // height: MediaQuery.of(context).size.height * 0.5,
    child: Text(
      'Hello World helloo wworiwoeiog hadfkjkdlfjj',
      textAlign: TextAlign.center,
      maxLines: 01,
      overflow: TextOverflow.ellipsis,
      //textScaleFactor: 2.2,
      semanticsLabel: "heading",
      style: TextStyle(
        fontFamily: 'Playball',
        fontWeight: FontWeight.w400,
        fontSize: 20,
        color: Colors.white,
        backgroundColor: Colors.brown,
        letterSpacing: 3,
        wordSpacing: 10,
        // fontStyle: ,
        decoration: TextDecoration.combine(
            [TextDecoration.underline, TextDecoration.overline]),
        decorationColor: Colors.white12,
        // decorationStyle:
        // shadows:
      ),
    ),
  ),
  'Day 4': DefaultTextStyle(
      style: TextStyle(
          fontFamily: 'Playball',
          backgroundColor: Colors.black,
          fontSize: 20,
          color: Colors.white),
      child: Column(
        children: [
          Text('Devil'),
          Text('Venom'),
          Text('SteelBlood'),
          Text('Zoro'),
        ],
      )),
};

// void tabbbbar(){
//
//   late TabController tabc;
//   @override
//   void initState() {
//     tabc = TabController(length: 2, vsync: this);
//     super.initState();
//   }
//
//   @override
//   void dispose() {
//     tabc.dispose();
//     super.dispose();
//   }
//
//
//
//
//
//   SingleChildScrollView(
//     child: Padding(
//       padding: const EdgeInsets.symmetric(horizontal: 20),
//       child: Column(
//         children: [
//           SizedBox(
//             height: 50,
//           ),
//           Container(
//             // height: 50,
//             width: MediaQuery.of(context).size.width,
//             decoration: BoxDecoration(
//                 color: Colors.teal,
//                 borderRadius: BorderRadius.circular(90)),
//             child: Column(
//               children: [
//                 Padding(
//                   padding: const EdgeInsets.all(5.0),
//                   child: TabBar(
//                     labelColor: Colors.white,
//                     unselectedLabelColor: Colors.black,
//                     indicatorColor: Colors.red,
//                     indicatorWeight: 2,
//                     dividerHeight: 0,
//                     indicator: BoxDecoration(
//                       color: Colors.red,
//                       borderRadius: BorderRadius.circular(90),
//                     ),
//                     indicatorSize: TabBarIndicatorSize.tab,
//                     controller: tabc,
//                     tabs: [
//                       Tab(
//                         text: 'Monthly',
//                       ),
//                       Tab(
//                         text: 'Weakly',
//                       )
//                     ],
//                   ),
//                 ),
//
//               ],
//             ),
//           ),
//           // Expanded(child: TabBarView(
//           //   children: [
//           //     Text('hello'),
//           //   ],
//           // )),
//         ],
//       ),
//     ),
//   )),
// }
