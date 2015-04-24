# Scriptic -- A Transliteration Tool

This project is for accurate cross-script tranliteration. It contains a bunch of
software, as well as dictionaries and other mappings that help in it.

Primary focus is on English(Language=English, Script=Latin) to
Devnagri(Language=English, Script=Devnagri).

Many Indian languages share a common alphabet, ka, kha, ga, but written
differently eg Hindi (क, ख, ग) vs Telgu (క, ఖ, గ). I think its the same sounds,
but written differently, and has different unicode characters assigned. I think
we may have been able to make do with same unicode characters codes and
different fonts too as well. That would have made this part of this project
redundent, but since its not so, this project can help you transliterate
Hindi(Language=Hindi, Script=Devnagri) to Telgu(Language=Hindi, Script=Devnagri)
or Telgu(Language=Telgu, Script=Telgu) to Hindi(Language=Telgu,
Script=Devnagri).


## Motivation

I am trying to create a transliteration thing.

Basically imagine a tool for my mom. She knows how to read and write Hindi well,
but does not know English. Now I want her to learn English, but learning English
means she has to learn two things simultaneously, the english language and
grammer/words etc, and reading/writing things.

Or consider one of my friend, whose domestic language is Telgu, but his wife
knows Hindi. Now she is learning Telgu, but making her learn a foreign looking
క, ఖ, గ, when its really क, ख, ग, is a wastage. She can already read and write
her name in Hindi, but Telgu speakers can read it. This tool will help her auto
transliterate to Telgu so Telgu speakers can read it, as well it will
transliterate Telgu texts like website content etc to Devnagri, so she can read
it (understanding it would be a different matter, she will have to learn the
words etc).

If you look at kids, they first learn grammar/words and then once they are
fluent they learn reading/writing.

If I can make reading writing easy for her, learning would be divided in two
separate phases, she can focus on words/grammar and not worry about
reading/writing in beginning.

Eventual goal is to write a browser extension, which transliterates everything,
but before that we need a basic transliteration library. And scriptic is an
effort towards that.


## Another Motivation -- Replace IPA with Devnagri

Wikipedia uses
[IPA](http://en.wikipedia.org/wiki/International_Phonetic_Alphabet), but IPA is
not capable of accurately representing sounds in all languages, devnagri has
bigger set of sounds. Also nearly no one can fluently read IPA (try reading
/ˈnjuːtən/, best of luck!), where as there are upwards of a 100 million who can
read devnagri. So this project also aims to replace IPA and other similar
schemes, eg the one used by [CMU](http://en.wikipedia.org/wiki/Arpabet)(try
reading B AA1 R B ER0 Z), or the one [Google uses](https://ww
w.dropbox.com/s/yu73fuf022psrq3/Screenshot%202015-04-20%2016.11.51.png?dl=0)(loo
ks like Khuṇ k̄hxbkhuṇ).

You see all these approaches are wrong. IPA, Arpabet, That Thing That Google
Uses, they are all reinventing crap after crap. They can't agree with each
other. Google chose to ignore both IPA and Arpabet, which are both standards
with significant volume of work done in. Because it was crap. But they only
created another crap, that nobody other than Google will use, and may be when
Apple realizes that Oh there are non english speakers in the world, they will
invent their own crap ignoring Googla/IPA/Arbabet. This must end.

One can argue that no English speaker will find "रीपॉसैटारी"" more readable than
"repository", but they will not find the IPA/Arpabet readable either. Google's
scheme would work for them though. But that is an English centric world view,
and the problem of "I can not pronounce English properly" is not a English
speaking world problem, but a problem of people with non English as a native
language. For them Google/IPA/Arpabet would be as hard as Devnagri, but at least
for close to billion people, they already know Devnagri (or Telgu etc versions
of them which this project supports).

May be world will never support, may be this will only make the job of Indians
better, so what, that alone is a worthy goal.


## Approach

Currently I am using [cmudict](https://github.com/cmusphinx/cmudict), which
lists English pronounciation code for some 40-50K words. I am [mapping those
codes to Devnagri](https://github.com/amitu/scriptic/blob/master/cmu.py#L25-L68).



## Result So Far

The second half of this page is auto transliterated with zero manual correction
using this tool.

Look at [the gist](https://gist.github.com/amitu/47e8438321d0b9e4b3cd) which
shows the conversion of 1000 most frequently used words in English language. It
is only 70-80% accurate so far. Even the accuracy rate is not known, as I am not
that great in English pronunciation myself.

## Help Me Please!

Fork the [gist](https://gist.github.com/amitu/47e8438321d0b9e4b3cd), and correct
it, and send me a mail. Or may be just mark the lines you think are wrong.

Any help with fixing cmu.py is highly appreciated too.

----

# Scriptic -- ऐ Transliteration टूल

दिस प्रॉजेक्ट इस फॉर ऐक्य्रैट क्रॉस-स्क्रिप्ट tranliteration. इट कैन्टेऽन्स ऐ बान्च आव
सॉफ्ट्वेर, ऐस वेल ऐस डिक्शैनेरीस ऐन्ड आदर mappings दैट हेल्प इन इट.

प्राय्मेरी फोकैस इस ऑन इंग्ग्लिश(लैंग्ग्वैज=इंग्ग्लिश, स्क्रिप्ट=लैटैन) टू
Devnagri(लैंग्ग्वैज=इंग्ग्लिश, स्क्रिप्ट=Devnagri).

मेनी इन्डीऐन लैंग्ग्वैजैस शेर ऐ कॉमैन ऐल्फैबेट, कॉ, kha, गॉ, बाट रिटैन
डिफ्रैन्ट्ली eg हिन्डी (क, ख, ग) वीएस Telgu (క, ఖ, గ). आय थिंग्क इट्स दै सेऽम साव्न्ड्स,
बाट रिटैन डिफ्रैन्ट्ली, ऐन्ड हैस डिफ्रैन्ट unicode कैरैक्ट्र्स ऐसाय्न्ड. आय थिंग्क
वी मेऽ हैव बिन एऽबैल टू मेऽक डू विद सेऽम unicode कैरैक्ट्र्स कोड्स ऐन्ड
डिफ्रैन्ट फॉन्ट्स टू ऐस वेल. दैट वूड हैव मेऽड दिस पॉर्ट आव दिस प्रॉजेक्ट
redundent, बाट सिन्स इट्स नॉट सो, दिस प्रॉजेक्ट कैन हेल्प यू transliterate
हिन्डी(लैंग्ग्वैज=हिन्डी, स्क्रिप्ट=Devnagri) टू Telgu(लैंग्ग्वैज=हिन्डी, स्क्रिप्ट=Devnagri)
ऑर Telgu(लैंग्ग्वैज=Telgu, स्क्रिप्ट=Telgu) टू हिन्डी(लैंग्ग्वैज=Telgu,
स्क्रिप्ट=Devnagri).


## मोटैवेऽशैन

आय ऐम ट्रायिंग टू क्रीएऽट ऐ transliteration थिंग.

बेऽसिक्ली इमैजैन ऐ टूल फॉर माय मॉम. शी नोस हाव टू रेड ऐन्ड राय्ट हिन्डी वेल,
बाट डास नॉट नो इंग्ग्लिश. नाव आय वॉन्ट हर टू ल्र्न इंग्ग्लिश, बाट ल्र्निंग इंग्ग्लिश
मीन्स शी हैस टू ल्र्न टू थिंग्स साय्मैल्टेऽनीऐस्ली, दै इंग्ग्लिश लैंग्ग्वैज ऐन्ड
ग्रैम्र/वर्ड्स एट्सेट्रै, ऐन्ड रीडिंग/राय्टिंग थिंग्स.

ऑर कैन्सिड्र वान आव माय फ्रेन्ड, हूस डैमेस्टिक लैंग्ग्वैज इस Telgu, बाट हिस वाय्फ
नोस हिन्डी. नाव शी इस ल्र्निंग Telgu, बाट मेऽकिंग हर ल्र्न ऐ फॉरैन लूकिंग
క, ఖ, గ, वेन इट्स रिली क, ख, ग, इस ऐ wastage. शी कैन आल्रेडी रेड ऐन्ड राय्ट
हर नेऽम इन हिन्डी, बाट Telgu स्पीक्र्स कैन रेड इट. दिस टूल विल हेल्प हर ऑटो
transliterate टू Telgu सो Telgu स्पीक्र्स कैन रेड इट, ऐस वेल इट विल
transliterate Telgu टेक्स्ट्स लाय्क वेब्साय्ट कॉन्टेन्ट एट्सेट्रै टू Devnagri, सो शी कैन रेड
इट (ऽन्ड्र्स्टैन्डिंग इट वूड बी ऐ डिफ्रैन्ट मैट्र, शी विल हैव टू ल्र्न दै
वर्ड्स एट्सेट्रै).

इफ यू लूक ऐट किड्स, देऽ फ्र्स्ट ल्र्न ग्रैम्र/वर्ड्स ऐन्ड देन वान्स देऽ ऑर
फ्लूऐन्ट देऽ ल्र्न रीडिंग/राय्टिंग.

इफ आय कैन मेऽक रीडिंग राय्टिंग ईसी फॉर हर, ल्र्निंग वूड बी डिवाय्डैड इन टू
सेप्रेऽट फेऽसैस, शी कैन फोकैस ऑन वर्ड्स/ग्रैम्र ऐन्ड नॉट वरी ऐबाव्ट
रीडिंग/राय्टिंग इन बिगिनिंग.

ऐवेन्चुऐल गोल इस टू राय्ट ऐ ब्राव्स्र इक्स्टेन्शैन, विच transliterates एव्रीथिंग,
बाट बिफॉर दैट वी नीड ऐ बेऽसिक transliteration लाय्ब्रेरी. ऐन्ड scriptic इस ऐन
एफ्र्ट टैवॉर्ड्स दैट.


## ऐनादर मोटैवेऽशैन -- रीप्लेऽस IPA विद Devnagri

विकीपीडीऐ यूसैस
[IPA](http://एन.विकीपीडीऐ.ऑर्ग/विकी/International_Phonetic_Alphabet), बाट IPA इस
नॉट केऽपैबैल आव ऐक्य्रैट्ली रेप्रिसेन्टिंग साव्न्ड्स इन ऑल लैंग्ग्वैजैस, devnagri हैस
बिग्र सेट आव साव्न्ड्स. ऑल्सो निर्ली नो वान कैन फ्लूऐन्ट्ली रेड IPA (ट्राय रीडिंग
/ˈnjuːटीəएन/, बेस्ट आव लाक!), वेर ऐस देर ऑर आप्वर्ड्स आव ऐ 100 मिल्यैन हू कैन
रेड devnagri. सो दिस प्रॉजेक्ट ऑल्सो एऽम्स टू रीप्लेऽस IPA ऐन्ड आदर सिमैल्र
स्कीम्स, eg दै वान यूस्ड बाय [सीएम्यू](http://एन.विकीपीडीऐ.ऑर्ग/विकी/Arpabet)(ट्राय
रीडिंग बी AA1 ऑर बी ER0 सी), ऑर दै वान [गूगैल यूसैस](https://ww
डाबैल्यु.dropbox.कॉम/एस/yu73fuf022psrq3/Screenshot%202015-04-20%2016.11.51.png?dl=0)(लू
ks लाय्क Khuṇ केऽ̄hxbkhuṇ).

यू सी ऑल दीस ऐप्रोचैस ऑर रॉंग. IPA, Arpabet, दैट थिंग दैट गूगैल
यूसैस, देऽ ऑर ऑल रीइन्वेन्टिंग क्रैप ऐफ्ट्र क्रैप. देऽ कैन'टी ऐग्री विद ईच
आदर. गूगैल चोस टू इग्नॉर बोथ IPA ऐन्ड Arpabet, विच ऑर बोथ स्टैन्ड्र्ड्स
विद सैग्निफिकैन्ट वॉल्युम आव वर्क डान इन. बिकॉस इट वॉस क्रैप. बाट देऽ ओन्ली
क्रीएऽटैड ऐनादर क्रैप, दैट नोबॉडी आदर दैन गूगैल विल यूस, ऐन्ड मेऽ बी वेन
ऐपैल रीऐलाय्सिस दैट ओ देर ऑर नॉन इंग्ग्लिश स्पीक्र्स इन दै वर्ल्ड, देऽ विल
इन्वेन्ट देर ओन क्रैप इग्नॉरिंग Googla/IPA/Arbabet. दिस मास्ट एन्ड.

वान कैन ऑर्ग्यु दैट नो इंग्ग्लिश स्पीक्र विल फाय्न्ड "रीपॉसैटारी"" मॉर रीडैबैल दैन
"रीपॉसैटारी", बाट देऽ विल नॉट फाय्न्ड दै IPA/Arpabet रीडैबैल ईदर. गूगैल'एस
स्कीम वूड वर्क फॉर देम दो. बाट दैट इस ऐन इंग्ग्लिश centric वर्ल्ड व्यू,
ऐन्ड दै प्रॉब्लैम आव "आय कैन नॉट प्रैनाव्न्स इंग्ग्लिश प्रॉप्र्ली" इस नॉट ऐ इंग्ग्लिश
स्पीकिंग वर्ल्ड प्रॉब्लैम, बाट ऐ प्रॉब्लैम आव पीपैल विद नॉन इंग्ग्लिश ऐस ऐ नेऽटिव
लैंग्ग्वैज. फॉर देम गूगैल/IPA/Arpabet वूड बी ऐस हॉर्ड ऐस Devnagri, बाट ऐट लीस्ट
फॉर क्लोस टू बिल्यैन पीपैल, देऽ आल्रेडी नो Devnagri (ऑर Telgu एट्सेट्रै व्र्सैन्स
आव देम विच दिस प्रॉजेक्ट सैपॉर्ट्स).

मेऽ बी वर्ल्ड विल नेव्र सैपॉर्ट, मेऽ बी दिस विल ओन्ली मेऽक दै जॉब आव इन्डीऐन्स
बेट्र, सो वाट, दैट ऐलोन इस ऐ वर्दी गोल.


## ऐप्रोच

क्रैन्ट्ली आय ऐम यूसिंग [cmudict](https://github.कॉम/cmusphinx/cmudict), विच
लिस्ट्स इंग्ग्लिश pronounciation कोड फॉर साम 40-50K वर्ड्स. आय ऐम [मैपिंग दोस
कोड्स टू Devnagri](https://github.कॉम/amitu/scriptic/ब्लॉब/मैस्ट्र/सीएम्यू.py#L25-L68).



## रिसाल्ट सो फॉर

दै सेकैन्ड हैफ आव दिस पेऽज इस ऑटो transliterated विद सिरो मैन्युऐल क्रेक्शैन
यूसिंग दिस टूल.

लूक ऐट [दै जिस्ट](https://जिस्ट.github.कॉम/amitu/47e8438321d0b9e4b3cd) विच
शोस दै कैन्व्र्सैन आव 1000 मोस्ट फ्रीक्वैन्ट्ली यूस्ड वर्ड्स इन इंग्ग्लिश लैंग्ग्वैज. इट
इस ओन्ली 70-80% ऐक्य्रैट सो फॉर. ईविन दै ऐक्य्रैसी रेऽट इस नॉट नोन, ऐस आय ऐम नॉट
दैट ग्रेऽट इन इंग्ग्लिश प्रोन्ऽन्सीएऽशैन माय्सेल्फ.

## हेल्प मी प्लीस!

फॉर्क दै [जिस्ट](https://जिस्ट.github.कॉम/amitu/47e8438321d0b9e4b3cd), ऐन्ड क्रेक्ट
इट, ऐन्ड सेन्ड मी ऐ मेऽल. ऑर मेऽ बी जास्ट मॉर्क दै लाय्न्स यू थिंग्क ऑर रॉंग.

एनी हेल्प विद फिक्सिंग सीएम्यू.py इस हाय्ली ऐप्रीशीएऽटिड टू.

