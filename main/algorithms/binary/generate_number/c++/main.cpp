byte[] bitfield = new byte [0xFFFFFFF/8];

void findOpenNumber2() throws FileNotFoundException {

    Scanner in = new Scanner(new FileReader("bigfile.txt"));

    while (in.hasNextInt()) {
        int n = in.nextInt ();
        /* Find n in bitfield, using OR for marking n-th bit in byte
         * (for example 10 will correspond to second bit in byte array)
        */
        bitfield [n / 8] |= 1 << (n % 8);
    }

    for (int i = 0; i < bitfield.length; i++) {
        for (int j = 0; j < 8; j++) {
          /*
            Get seperate bits of every byte. When found 0, find corresponding
            integer
          */
            if ((bitfield[i] & (1 << j)) == 0) {
                System.out.println(i * 8 + j);
                return;
            }
        }
    }
}
