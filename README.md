# हिन्दिक

A repository containing devnagri/hindi transliteration of words in English and
possibly other languages.

The repository would be composed of text files with lines like:

example: इग्ज़ाम्पल (उदाहरड़) - Not sure if to use ज़ or झ there.

Syntax: Word phrase in foreign language, followed by colon, followed by
word/phrase in Hindi, followed by optional meaning of foreign word in Hindi in
parenthesis, followed by optional - and comments.



## Motivation

I am trying to create a transliteration thing.

Basically imagine a tool for my mom. Now I want her to learn English, but learning English means she has to learn two things simultaneously, the english language and grammer/words etc, and reading/writing things.

If you look at kids, they first learn grammar/words and then once they are fluent they learn reading/writing.

If I can make reading writing easy for her, learning would be divided in two separate phases, she can focus on words/grammar and not worry about reading/writing in beginning.

Eventual goal is to write a browser extension, which transliterates everything to hindic, but before that we need a basic transliteration library. And hindic is an effort towards that.



## Approach

Currently I am using [cmudict](https://github.com/cmusphinx/cmudict), which
lists English pronounciation code for some 40-50K words. I am [mapping those
codes to Devnagri](https://github.com/amitu/hindic/blob/master/cmu.py#L25-L68).



## Result So Far

Look at [the gist](https://gist.github.com/amitu/47e8438321d0b9e4b3cd) which
shows the conversion of 1000 most frequently used words in English language. It
is only 70-80% accurate so far. Even the accuracy rate is not known, as I am not
that great in English pronunciation myself.



## Help Me Please!

Fork the [gist](https://gist.github.com/amitu/47e8438321d0b9e4b3cd), and correct
it, and send me a mail. Or may be just mark the lines you think are wrong.

Any help with fixing cmu.py is highly appreciated too.

----

# हिन्दिक

ऐ रीपॉसैटारी कैन्टेऽनिंग devnagri/हिन्डी transliteration आव वर्ड्स इन इंग्ग्लिश ऐन्ड
पॉसैब्ली आदर लैंग्ग्वैजैस.

दै रीपॉसैटारी वूड बी कैम्पोस्ड आव टेक्स्ट फाय्ल्स विद लाय्न्स लाय्क:

इग्सैम्पैल: इग्ज़ाम्पल (उदाहरड़) - नॉट शूर इफ टू यूस ज़ ऑर झ देर.

सिन्टैक्स: वर्ड फ्रेऽस इन फॉरैन लैंग्ग्वैज, फॉलोड बाय कोलैन, फॉलोड बाय
वर्ड/फ्रेऽस इन हिन्डी, फॉलोड बाय ऑप्शैनैल मीनिंग आव फॉरैन वर्ड इन हिन्डी इन
प्रेन्थैसिस, फॉलोड बाय ऑप्शैनैल - ऐन्ड कॉमेन्ट्स.



## मोटैवेऽशैन

आय ऐम ट्रायिंग टू क्रीएऽट ऐ transliteration थिंग.

बेऽसिक्ली इमैजैन ऐ टूल फॉर माय मॉम. नाव आय वॉन्ट हर टू ल्र्न इंग्ग्लिश, बाट ल्र्निंग इंग्ग्लिश मीन्स शी हैस टू ल्र्न टू थिंग्स साय्मैल्टेऽनीऐस्ली, दै इंग्ग्लिश लैंग्ग्वैज ऐन्ड ग्रैम्र/वर्ड्स एट्सेट्रै, ऐन्ड रीडिंग/राय्टिंग थिंग्स.

इफ यू लूक ऐट किड्स, देऽ फ्र्स्ट ल्र्न ग्रैम्र/वर्ड्स ऐन्ड देन वान्स देऽ ऑर फ्लूऐन्ट देऽ ल्र्न रीडिंग/राय्टिंग.

इफ आय कैन मेऽक रीडिंग राय्टिंग ईसी फॉर हर, ल्र्निंग वूड बी डिवाय्डैड इन टू सेप्रेऽट फेऽसैस, शी कैन फोकैस ऑन वर्ड्स/ग्रैम्र ऐन्ड नॉट वरी ऐबाव्ट रीडिंग/राय्टिंग इन बिगिनिंग.

ऐवेन्चुऐल गोल इस टू राय्ट ऐ ब्राव्स्र इक्स्टेन्शैन, विच transliterates एव्रीथिंग टू hindic, बाट बिफॉर दैट वी नीड ऐ बेऽसिक transliteration लाय्ब्रेरी. ऐन्ड hindic इस ऐन एफ्र्ट टैवॉर्ड्स दैट.



## ऐप्रोच

क्रैन्ट्ली आय ऐम यूसिंग [cmudict](https://github.कॉम/cmusphinx/cmudict), विच
लिस्ट्स इंग्ग्लिश pronounciation कोड फॉर साम 40-50K वर्ड्स. आय ऐम [मैपिंग दोस
कोड्स टू Devnagri](https://github.कॉम/amitu/hindic/ब्लॉब/मैस्ट्र/सीएम्यू.py#L25-L68).



## रिसाल्ट सो फॉर

लूक ऐट [दै जिस्ट](https://जिस्ट.github.कॉम/amitu/47e8438321d0b9e4b3cd) विच
शोस दै कैन्व्र्सैन आव 1000 मोस्ट फ्रीक्वैन्ट्ली यूस्ड वर्ड्स इन इंग्ग्लिश लैंग्ग्वैज. इट
इस ओन्ली 70-80% ऐक्य्रैट सो फॉर. ईविन दै ऐक्य्रैसी रेऽट इस नॉट नोन, ऐस आय ऐम नॉट
दैट ग्रेऽट इन इंग्ग्लिश प्रोन्ऽन्सीएऽशैन माय्सेल्फ.



## हेल्प मी प्लीस!

फॉर्क दै [जिस्ट](https://जिस्ट.github.कॉम/amitu/47e8438321d0b9e4b3cd), ऐन्ड क्रेक्ट
इट, ऐन्ड सेन्ड मी ऐ मेऽल. ऑर मेऽ बी जास्ट मॉर्क दै लाय्न्स यू थिंग्क ऑर रॉंग.

एनी हेल्प विद फिक्सिंग सीएम्यू.py इस हाय्ली ऐप्रीशीएऽटिड टू.

