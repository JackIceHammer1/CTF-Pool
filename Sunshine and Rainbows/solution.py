import hashlib

#hashes = ["5569eaa76a31252a24cce3f9f7649dc6c1b92420754fd0b344307acbb94a91e4","a2c69ee247a4135d1fa9913c84145920f92fa3f19a187f61ab6e6d1ff0f7f219","0b529fa24b53a6c1a00756502a8ed2a41328bfac802e36152da26701b51a0b42","8febde718070b1edb9f8fb2e4cf004dd3b9616c50998bd0cf9de12db29fe0cc0","bdeda68cdc11971120649097036aefa65845d525e05beb4b737943f3ae0a14e1"]

#rainbow = [["63ce7240","8276231ec0e2a8afaaf61404022a3eecb866bba918fc63040458a1eea6f1d3b1"],["67811714","c9a14d2210315cfdf408aaca4eac4d54be5b1e537c9cb25993c0736d2c27b943"],["d5ac5c2d","183eab7776a93b17302c4c4f14a016bde80f8e66b72666efea9b0aabac05891c"],["84af9342","230549f64a0fcba576f4aa9b8983a7f52237e0ef5901fdfba17d3e6815793657"],["fcc2a316","b09fa27c46ad5e1c2507fd5dab1f607b7f6a855efb83787655b77c323aa91c53"]]

#r2 = [b"8276231ec0e2a8afaaf61404022a3eecb866bba918fc63040458a1eea6f1d3b1",b"63ce7240",b"c9a14d2210315cfdf408aaca4eac4d54be5b1e537c9cb25993c0736d2c27b943",b"67811714",b"183eab7776a93b17302c4c4f14a016bde80f8e66b72666efea9b0aabac05891c",b"d5ac5c2d", b"230549f64a0fcba576f4aa9b8983a7f52237e0ef5901fdfba17d3e6815793657" ,b"84af9342",b"b09fa27c46ad5e1c2507fd5dab1f607b7f6a855efb83787655b77c323aa91c53",b"fcc2a316"]

#print(hashlib.sha256(b"95348d25fc246e6f6e1e1124b25226c175dfbfa806142974a5fd255c9c909d28"[0:8]).hexdigest()[0:8])

hashes = ["a3c22a6ed9cac701d890f4df9ea0f9cd78b33900f72fda2cc126eb1bc572b317"]

rainbow = [["b186069a", "e3c66cc8dc56075dbdf862d6127087010490b9c7719b26586fa522550c87f3b5"],["c06bc6b7", "e20d0ba6a2c15ad13930f9a13fef9d41e31cbe66931b9483531eac7036408020"], ["af5cd77b","9661c88d36de19143d2399df1f0716ea7b32bd32f9f7df1772752df7a0a41bbc"]]

for b in hashes:
    hash = b
    for a in range(0, 132):
        for c in rainbow:
            if hash[0:8] == c[1][0:8]:
                print("Match",b,c,a)
                previous = ""
                p = c[0]
                for x in range(0,132):
                    if p[0:8] == b[0:8]:
                        print("Solution", previous[0:8])
                        p = hashlib.sha256(p[0:8].encode('utf-8')).hexdigest()
                    previous=p
                    p = hashlib.sha256(p[0:8].encode('utf-8')).hexdigest()
                    
                
                
        hash = hashlib.sha256(hash[0:8].encode('utf-8')).hexdigest()

            


