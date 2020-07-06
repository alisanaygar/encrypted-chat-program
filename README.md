# encrypted-chat-program
 Encrypted Chat Program Using RSA and AES

In this project, Alice selects a random symmetric session key, Ks, encrypts her message, m, with the symmetric key, encrypts the symmetric key with Bob’s public key, Kb+, concatenates the encrypted message and the encrypted symmetric key to form a “package” and sends the package to Bob’s e-mail address. The steps are illustrated in Figure 1. (In this and the subsequent figures, the circled “+” represents concatenation and the circled “–” represents deconcatenation.) When Bob receives the package, he uses his private key, Kb–, to obtain the symmetric key, Ks, and uses the symmetric key Ks to decrypt the message m.

![image](https://user-images.githubusercontent.com/62813539/86625578-f18d6d80-bfcd-11ea-96dc-d85ff8c26f0b.png)

I created a flow-diagram of this project.

![image](https://user-images.githubusercontent.com/62813539/86625674-1f72b200-bfce-11ea-9e89-cd2efda2e17b.png)
