# encrypted-chat-program
 Encrypted Chat Program Using RSA and AES

In this project, Alice selects a random symmetric session key, Ks, encrypts her message, m, with the symmetric key, encrypts the symmetric key with Bob’s public key, Kb+, concatenates the encrypted message and the encrypted symmetric key to form a “package” and sends the package to Bob’s e-mail address. The steps are illustrated in Figure 1. (In this and the subsequent figures, the circled “+” represents concatenation and the circled “–” represents deconcatenation.) When Bob receives the package, he uses his private key, Kb–, to obtain the symmetric key, Ks, and uses the symmetric key Ks to decrypt the message m.

![Alice used a symmetric session key, KS, to send a secret e-mail to Bob](/images/logo.png)
