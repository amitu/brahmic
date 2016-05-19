# ब्राह्मिक - A Transliteration Tool

This project is for accurate cross-script tranliteration. It contains a bunch of
software, as well as dictionaries and other mappings that help in it.

Primary focus is on English(Language=English, Script=Latin) to
Devanagari(Language=English, Script=Devanagari).

Many Indian languages share a common alphabet, ka, kha, ga, but written
differently eg Hindi (क, ख, ग) vs Telugu (క, ఖ, గ). I think its the same sounds,
but written differently, and has different unicode characters assigned. I think
we may have been able to make do with same unicode characters codes and
different fonts too as well. That would have made this part of this project
redundant, but since its not so, this project can help you transliterate
Hindi(Language=Hindi, Script=Devanagari) to Telugu(Language=Hindi, Script=Devanagari)
or Telugu(Language=Telugu, Script=Telugu) to Hindi(Language=Telugu,
Script=Devanagari).


## Motivation

I am trying to create a transliteration thing.

Basically imagine a tool for my mom. She knows how to read and write Hindi well,
but does not know English. Now I want her to learn English, but learning English
means she has to learn two things simultaneously, the english language and
grammer/words etc, and reading/writing things.

Or consider one of my friend, whose domestic language is Telugu, but his wife
knows Hindi. Now she is learning Telugu, but making her learn a foreign looking
క, ఖ, గ, when its really क, ख, ग, is a wastage. She can already read and write
her name in Hindi, but Telugu speakers can read it. This tool will help her auto
transliterate to Telugu so Telugu speakers can read it, as well it will
transliterate Telugu texts like website content etc to Devanagari, so she can read
it (understanding it would be a different matter, she will have to learn the
words etc).

If you look at kids, they first learn grammar/words and then once they are
fluent they learn reading/writing.

If I can make reading writing easy for her, learning would be divided in two
separate phases, she can focus on words/grammar and not worry about
reading/writing in beginning.

Eventual goal is to write a browser extension, which transliterates everything,
but before that we need a basic transliteration library. And ब्राह्मिक is an
effort towards that.


## Another Motivation - Replace IPA with Devanagari

Wikipedia uses
[IPA](http://en.wikipedia.org/wiki/International_Phonetic_Alphabet), but IPA is
not capable of accurately representing sounds in all languages, devnagri has
bigger set of sounds. Also nearly no one can fluently read IPA (try reading
/ˈnjuːtən/, best of luck!), where as there are upwards of a 100 million who can
read devnagri. So this project also aims to replace IPA and other similar
schemes, eg the one used by [CMU](http://en.wikipedia.org/wiki/Arpabet)(try
reading B AA1 R B ER0 Z), or the one [Google uses](https://www.dropbox.com/s/yu
73fuf022psrq3/Screenshot%202015-04-20%2016.11.51.png?dl=0)(looks like Khuṇ
k̄hxbkhuṇ).

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
language. For them Google/IPA/Arpabet would be as hard as Devanagari, but at least
for close to billion people, they already know Devanagari (or some other [Brahmic
Script](http://en.wikipedia.org/wiki/Brahmic_scripts)).

May be world will never support, may be this will only make the job of Indians
better, so what, that alone is a worthy goal.


## Approach

Currently I am using [cmudict](https://github.com/cmusphinx/cmudict), which
lists English pronounciation code for some 40-50K words. I am [mapping those
codes to Devanagari](https://github.com/amitu/brahmic/blob/master/cmu.py#L25-L68).



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

# ब्राह्मिक - ऐ Transliteration टूल

दिस प्रॉजेक्ट इस फॉर ऐक्य्रैट क्रॉस-स्क्रिप्ट tranliteration. इट कैन्टेऽन्स ऐ बान्च आव
सॉफ्ट्वेर, ऐस वेल ऐस डिक्शैनेरीस ऐन्ड आदर mappings दैट हेल्प इन इट.

प्राय्मेरी फोकैस इस ऑन इंग्ग्लिश(लैंग्ग्वैज=इंग्ग्लिश, स्क्रिप्ट=लैटैन) टू
Devanagari(लैंग्ग्वैज=इंग्ग्लिश, स्क्रिप्ट=Devanagari).

मेनी इन्डीऐन लैंग्ग्वैजैस शेर ऐ कॉमैन ऐल्फैबेट, कॉ, kha, गॉ, बाट रिटैन
डिफ्रैन्ट्ली eg हिन्डी (क, ख, ग) वीएस टेलूगु (క, ఖ, గ). आय थिंग्क इट्स दै सेऽम साव्न्ड्स,
बाट रिटैन डिफ्रैन्ट्ली, ऐन्ड हैस डिफ्रैन्ट unicode कैरैक्ट्र्स ऐसाय्न्ड. आय थिंग्क
वी मेऽ हैव बिन एऽबैल टू मेऽक डू विद सेऽम unicode कैरैक्ट्र्स कोड्स ऐन्ड
डिफ्रैन्ट फॉन्ट्स टू ऐस वेल. दैट वूड हैव मेऽड दिस पॉर्ट आव दिस प्रॉजेक्ट
रिडान्डैन्ट, बाट सिन्स इट्स नॉट सो, दिस प्रॉजेक्ट कैन हेल्प यू transliterate
हिन्डी(लैंग्ग्वैज=हिन्डी, स्क्रिप्ट=Devanagari) टू टेलूगु(लैंग्ग्वैज=हिन्डी, स्क्रिप्ट=Devanagari)
ऑर टेलूगु(लैंग्ग्वैज=टेलूगु, स्क्रिप्ट=टेलूगु) टू हिन्डी(लैंग्ग्वैज=टेलूगु,
स्क्रिप्ट=Devanagari).


## मोटैवेऽशैन

आय ऐम ट्रायिंग टू क्रीएऽट ऐ transliteration थिंग.

बेऽसिक्ली इमैजैन ऐ टूल फॉर माय मॉम. शी नोस हाव टू रेड ऐन्ड राय्ट हिन्डी वेल,
बाट डास नॉट नो इंग्ग्लिश. नाव आय वॉन्ट हर टू ल्र्न इंग्ग्लिश, बाट ल्र्निंग इंग्ग्लिश
मीन्स शी हैस टू ल्र्न टू थिंग्स साय्मैल्टेऽनीऐस्ली, दै इंग्ग्लिश लैंग्ग्वैज ऐन्ड
ग्रैम्र/वर्ड्स एट्सेट्रै, ऐन्ड रीडिंग/राय्टिंग थिंग्स.

ऑर कैन्सिड्र वान आव माय फ्रेन्ड, हूस डैमेस्टिक लैंग्ग्वैज इस टेलूगु, बाट हिस वाय्फ
नोस हिन्डी. नाव शी इस ल्र्निंग टेलूगु, बाट मेऽकिंग हर ल्र्न ऐ फॉरैन लूकिंग
క, ఖ, గ, वेन इट्स रिली क, ख, ग, इस ऐ wastage. शी कैन आल्रेडी रेड ऐन्ड राय्ट
हर नेऽम इन हिन्डी, बाट टेलूगु स्पीक्र्स कैन रेड इट. दिस टूल विल हेल्प हर ऑटो
transliterate टू टेलूगु सो टेलूगु स्पीक्र्स कैन रेड इट, ऐस वेल इट विल
transliterate टेलूगु टेक्स्ट्स लाय्क वेब्साय्ट कॉन्टेन्ट एट्सेट्रै टू Devanagari, सो शी कैन रेड
इट (ऽन्ड्र्स्टैन्डिंग इट वूड बी ऐ डिफ्रैन्ट मैट्र, शी विल हैव टू ल्र्न दै
वर्ड्स एट्सेट्रै).

इफ यू लूक ऐट किड्स, देऽ फ्र्स्ट ल्र्न ग्रैम्र/वर्ड्स ऐन्ड देन वान्स देऽ ऑर
फ्लूऐन्ट देऽ ल्र्न रीडिंग/राय्टिंग.

इफ आय कैन मेऽक रीडिंग राय्टिंग ईसी फॉर हर, ल्र्निंग वूड बी डिवाय्डैड इन टू
सेप्रेऽट फेऽसैस, शी कैन फोकैस ऑन वर्ड्स/ग्रैम्र ऐन्ड नॉट वरी ऐबाव्ट
रीडिंग/राय्टिंग इन बिगिनिंग.

ऐवेन्चुऐल गोल इस टू राय्ट ऐ ब्राव्स्र इक्स्टेन्शैन, विच transliterates एव्रीथिंग,
बाट बिफॉर दैट वी नीड ऐ बेऽसिक transliteration लाय्ब्रेरी. ऐन्ड ब्राह्मिक इस ऐन
एफ्र्ट टैवॉर्ड्स दैट.


## ऐनादर मोटैवेऽशैन - रीप्लेऽस IPA विद Devanagari

विकीपीडीऐ यूसैस
[IPA](http://एन.विकीपीडीऐ.ऑर्ग/विकी/International_Phonetic_Alphabet), बाट IPA इस
नॉट केऽपैबैल आव ऐक्य्रैट्ली रेप्रिसेन्टिंग साव्न्ड्स इन ऑल लैंग्ग्वैजैस, devnagri हैस
बिग्र सेट आव साव्न्ड्स. ऑल्सो निर्ली नो वान कैन फ्लूऐन्ट्ली रेड IPA (ट्राय रीडिंग
/ˈnjuːटीəएन/, बेस्ट आव लाक!), वेर ऐस देर ऑर आप्वर्ड्स आव ऐ 100 मिल्यैन हू कैन
रेड devnagri. सो दिस प्रॉजेक्ट ऑल्सो एऽम्स टू रीप्लेऽस IPA ऐन्ड आदर सिमैल्र
स्कीम्स, eg दै वान यूस्ड बाय [सीएम्यू](http://एन.विकीपीडीऐ.ऑर्ग/विकी/Arpabet)(ट्राय
रीडिंग बी AA1 ऑर बी ER0 सी), ऑर दै वान [गूगैल यूसैस](https://www.dropbox.कॉम/एस/यू
73fuf022psrq3/Screenshot%202015-04-20%2016.11.51.png?dl=0)(लूक्स लाय्क Khuṇ
केऽ̄hxbkhuṇ).

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
लैंग्ग्वैज. फॉर देम गूगैल/IPA/Arpabet वूड बी ऐस हॉर्ड ऐस Devanagari, बाट ऐट लीस्ट
फॉर क्लोस टू बिल्यैन पीपैल, देऽ आल्रेडी नो Devanagari (ऑर साम आदर [Brahmic
स्क्रिप्ट](http://एन.विकीपीडीऐ.ऑर्ग/विकी/Brahmic_scripts)).

मेऽ बी वर्ल्ड विल नेव्र सैपॉर्ट, मेऽ बी दिस विल ओन्ली मेऽक दै जॉब आव इन्डीऐन्स
बेट्र, सो वाट, दैट ऐलोन इस ऐ वर्दी गोल.


## ऐप्रोच

क्रैन्ट्ली आय ऐम यूसिंग [cmudict](https://github.कॉम/cmusphinx/cmudict), विच
लिस्ट्स इंग्ग्लिश pronounciation कोड फॉर साम 40-50K वर्ड्स. आय ऐम [मैपिंग दोस
कोड्स टू Devanagari](https://github.कॉम/amitu/brahmic/ब्लॉब/मैस्ट्र/सीएम्यू.py#L25-L68).



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

----

# బ్రాహ్మిక - ఐ Transliteration టూల్

దిస్ ప్రాజెక్ట్ ఇస్ ఫార్ ఐక్య్రైట్ క్రాస్-స్క్రిప్ట్ tranliteration. ఇట్ కైన్టెఽన్స్ ఐ బాన్చ ఆవ్
సాఫ్ట్వెర్, ఐస్ వెల్ ఐస్ డిక్శైనెరీస్ ఐన్డ్ ఆదర్ mappings దైట్ హెల్ప్ ఇన్ ఇట్.

ప్రాయ్మెరీ ఫొకైస్ ఇస్ ఆన్ ఇంగ్గ్లిశ(లైంగ్గ్వైజ్=ఇంగ్గ్లిశ, స్క్రిప్ట్=లైటైన్) టూ
Devanagari(లైంగ్గ్వైజ్=ఇంగ్గ్లిశ, స్క్రిప్ట్=Devanagari).

మెనీ ఇన్డీఐన్ లైంగ్గ్వైజైస్ శెర్ ఐ కామైన్ ఐల్ఫైబెట్, కా, kha, గా, బాట్ రిటైన్
డిఫ్రైన్ట్లీ eg హిన్డీ (క, ఖ, గ) వీఎస్ టెలూగు (క, ఖ, గ). ఆయ్ థింగ్క్ ఇట్స్ దై సెఽమ్ సావ్న్డ్స్,
బాట్ రిటైన్ డిఫ్రైన్ట్లీ, ఐన్డ్ హైస్ డిఫ్రైన్ట్ unicode కైరైక్ట్ర్స్ ఐసాయ్న్డ్. ఆయ్ థింగ్క్
వీ మెఽ హైవ్ బిన్ ఎఽబైల్ టూ మెఽక్ డూ విద సెఽమ్ unicode కైరైక్ట్ర్స్ కొడ్స్ ఐన్డ్
డిఫ్రైన్ట్ ఫాన్ట్స్ టూ ఐస్ వెల్. దైట్ వూడ్ హైవ్ మెఽడ్ దిస్ పార్ట్ ఆవ్ దిస్ ప్రాజెక్ట్
రిడాన్డైన్ట్, బాట్ సిన్స్ ఇట్స్ నాట్ సొ, దిస్ ప్రాజెక్ట్ కైన్ హెల్ప్ యూ transliterate
హిన్డీ(లైంగ్గ్వైజ్=హిన్డీ, స్క్రిప్ట్=Devanagari) టూ టెలూగు(లైంగ్గ్వైజ్=హిన్డీ, స్క్రిప్ట్=Devanagari)
ఆర్ టెలూగు(లైంగ్గ్వైజ్=టెలూగు, స్క్రిప్ట్=టెలూగు) టూ హిన్డీ(లైంగ్గ్వైజ్=టెలూగు,
స్క్రిప్ట్=Devanagari).


## మొటైవెఽశైన్

ఆయ్ ఐమ్ ట్రాయింగ్ టూ క్రీఎఽట్ ఐ transliteration థింగ్.

బెఽసిక్లీ ఇమైజైన్ ఐ టూల్ ఫార్ మాయ్ మామ్. శీ నొస్ హావ్ టూ రెడ్ ఐన్డ్ రాయ్ట్ హిన్డీ వెల్,
బాట్ డాస్ నాట్ నొ ఇంగ్గ్లిశ. నావ్ ఆయ్ వాన్ట్ హర్ టూ ల్ర్న్ ఇంగ్గ్లిశ, బాట్ ల్ర్నింగ్ ఇంగ్గ్లిశ
మీన్స్ శీ హైస్ టూ ల్ర్న్ టూ థింగ్స్ సాయ్మైల్టెఽనీఐస్లీ, దై ఇంగ్గ్లిశ లైంగ్గ్వైజ్ ఐన్డ్
గ్రైమ్ర్/వర్డ్స్ ఎట్సెట్రై, ఐన్డ్ రీడింగ్/రాయ్టింగ్ థింగ్స్.

ఆర్ కైన్సిడ్ర్ వాన్ ఆవ్ మాయ్ ఫ్రెన్డ్, హూస్ డైమెస్టిక్ లైంగ్గ్వైజ్ ఇస్ టెలూగు, బాట్ హిస్ వాయ్ఫ్
నొస్ హిన్డీ. నావ్ శీ ఇస్ ల్ర్నింగ్ టెలూగు, బాట్ మెఽకింగ్ హర్ ల్ర్న్ ఐ ఫారైన్ లూకింగ్
క, ఖ, గ, వెన్ ఇట్స్ రిలీ క, ఖ, గ, ఇస్ ఐ wastage. శీ కైన్ ఆల్రెడీ రెడ్ ఐన్డ్ రాయ్ట్
హర్ నెఽమ్ ఇన్ హిన్డీ, బాట్ టెలూగు స్పీక్ర్స్ కైన్ రెడ్ ఇట్. దిస్ టూల్ విల్ హెల్ప్ హర్ ఆటొ
transliterate టూ టెలూగు సొ టెలూగు స్పీక్ర్స్ కైన్ రెడ్ ఇట్, ఐస్ వెల్ ఇట్ విల్
transliterate టెలూగు టెక్స్ట్స్ లాయ్క్ వెబ్సాయ్ట్ కాన్టెన్ట్ ఎట్సెట్రై టూ Devanagari, సొ శీ కైన్ రెడ్
ఇట్ (ఽన్డ్ర్స్టైన్డింగ్ ఇట్ వూడ్ బీ ఐ డిఫ్రైన్ట్ మైట్ర్, శీ విల్ హైవ్ టూ ల్ర్న్ దై
వర్డ్స్ ఎట్సెట్రై).

ఇఫ్ యూ లూక్ ఐట్ కిడ్స్, దెఽ ఫ్ర్స్ట్ ల్ర్న్ గ్రైమ్ర్/వర్డ్స్ ఐన్డ్ దెన్ వాన్స్ దెఽ ఆర్
ఫ్లూఐన్ట్ దెఽ ల్ర్న్ రీడింగ్/రాయ్టింగ్.

ఇఫ్ ఆయ్ కైన్ మెఽక్ రీడింగ్ రాయ్టింగ్ ఈసీ ఫార్ హర్, ల్ర్నింగ్ వూడ్ బీ డివాయ్డైడ్ ఇన్ టూ
సెప్రెఽట్ ఫెఽసైస్, శీ కైన్ ఫొకైస్ ఆన్ వర్డ్స్/గ్రైమ్ర్ ఐన్డ్ నాట్ వరీ ఐబావ్ట్
రీడింగ్/రాయ్టింగ్ ఇన్ బిగినింగ్.

ఐవెన్చుఐల్ గొల్ ఇస్ టూ రాయ్ట్ ఐ బ్రావ్స్ర్ ఇక్స్టెన్శైన్, విచ transliterates ఎవ్రీథింగ్,
బాట్ బిఫార్ దైట్ వీ నీడ్ ఐ బెఽసిక్ transliteration లాయ్బ్రెరీ. ఐన్డ్ బ్రాహ్మిక ఇస్ ఐన్
ఎఫ్ర్ట్ టైవార్డ్స్ దైట్.


## ఐనాదర్ మొటైవెఽశైన్ - రీప్లెఽస్ IPA విద Devanagari

వికీపీడీఐ యూసైస్
[IPA](http://ఎన్.వికీపీడీఐ.ఆర్గ్/వికీ/International_Phonetic_Alphabet), బాట్ IPA ఇస్
నాట్ కెఽపైబైల్ ఆవ్ ఐక్య్రైట్లీ రెప్రిసెన్టింగ్ సావ్న్డ్స్ ఇన్ ఆల్ లైంగ్గ్వైజైస్, devnagri హైస్
బిగ్ర్ సెట్ ఆవ్ సావ్న్డ్స్. ఆల్సొ నిర్లీ నొ వాన్ కైన్ ఫ్లూఐన్ట్లీ రెడ్ IPA (ట్రాయ్ రీడింగ్
/ˈnjuːటీəఎన్/, బెస్ట్ ఆవ్ లాక్!), వెర్ ఐస్ దెర్ ఆర్ ఆప్వర్డ్స్ ఆవ్ ఐ ౧౦౦ మిల్యైన్ హూ కైన్
రెడ్ devnagri. సొ దిస్ ప్రాజెక్ట్ ఆల్సొ ఎఽమ్స్ టూ రీప్లెఽస్ IPA ఐన్డ్ ఆదర్ సిమైల్ర్
స్కీమ్స్, eg దై వాన్ యూస్డ్ బాయ్ [సీఎమ్యూ](http://ఎన్.వికీపీడీఐ.ఆర్గ్/వికీ/Arpabet)(ట్రాయ్
రీడింగ్ బీ AA౧ ఆర్ బీ ER౦ సీ), ఆర్ దై వాన్ [గూగైల్ యూసైస్](https://www.dropbox.కామ్/ఎస్/యూ
౭౩fuf౦౨౨psrq౩/Screenshot%౨౦౨౦౧౫-౦౪-౨౦%౨౦౧౬.౧౧.౫౧.png?dl=౦)(లూక్స్ లాయ్క్ Khuṇ
కెఽ̄hxbkhuṇ).

యూ సీ ఆల్ దీస్ ఐప్రొచైస్ ఆర్ రాంగ్. IPA, Arpabet, దైట్ థింగ్ దైట్ గూగైల్
యూసైస్, దెఽ ఆర్ ఆల్ రీఇన్వెన్టింగ్ క్రైప్ ఐఫ్ట్ర్ క్రైప్. దెఽ కైన్'టీ ఐగ్రీ విద ఈచ
ఆదర్. గూగైల్ చొస్ టూ ఇగ్నార్ బొథ IPA ఐన్డ్ Arpabet, విచ ఆర్ బొథ స్టైన్డ్ర్డ్స్
విద సైగ్నిఫికైన్ట్ వాల్యుమ్ ఆవ్ వర్క్ డాన్ ఇన్. బికాస్ ఇట్ వాస్ క్రైప్. బాట్ దెఽ ఓన్లీ
క్రీఎఽటైడ్ ఐనాదర్ క్రైప్, దైట్ నొబాడీ ఆదర్ దైన్ గూగైల్ విల్ యూస్, ఐన్డ్ మెఽ బీ వెన్
ఐపైల్ రీఐలాయ్సిస్ దైట్ ఓ దెర్ ఆర్ నాన్ ఇంగ్గ్లిశ స్పీక్ర్స్ ఇన్ దై వర్ల్డ్, దెఽ విల్
ఇన్వెన్ట్ దెర్ ఓన్ క్రైప్ ఇగ్నారింగ్ Googla/IPA/Arbabet. దిస్ మాస్ట్ ఎన్డ్.

వాన్ కైన్ ఆర్గ్యు దైట్ నొ ఇంగ్గ్లిశ స్పీక్ర్ విల్ ఫాయ్న్డ్ "రీపాసైటారీ"" మార్ రీడైబైల్ దైన్
"రీపాసైటారీ", బాట్ దెఽ విల్ నాట్ ఫాయ్న్డ్ దై IPA/Arpabet రీడైబైల్ ఈదర్. గూగైల్'ఎస్
స్కీమ్ వూడ్ వర్క్ ఫార్ దెమ్ దొ. బాట్ దైట్ ఇస్ ఐన్ ఇంగ్గ్లిశ centric వర్ల్డ్ వ్యూ,
ఐన్డ్ దై ప్రాబ్లైమ్ ఆవ్ "ఆయ్ కైన్ నాట్ ప్రైనావ్న్స్ ఇంగ్గ్లిశ ప్రాప్ర్లీ" ఇస్ నాట్ ఐ ఇంగ్గ్లిశ
స్పీకింగ్ వర్ల్డ్ ప్రాబ్లైమ్, బాట్ ఐ ప్రాబ్లైమ్ ఆవ్ పీపైల్ విద నాన్ ఇంగ్గ్లిశ ఐస్ ఐ నెఽటివ్
లైంగ్గ్వైజ్. ఫార్ దెమ్ గూగైల్/IPA/Arpabet వూడ్ బీ ఐస్ హార్డ్ ఐస్ Devanagari, బాట్ ఐట్ లీస్ట్
ఫార్ క్లొస్ టూ బిల్యైన్ పీపైల్, దెఽ ఆల్రెడీ నొ Devanagari (ఆర్ సామ్ ఆదర్ [Brahmic
స్క్రిప్ట్](http://ఎన్.వికీపీడీఐ.ఆర్గ్/వికీ/Brahmic_scripts)).

మెఽ బీ వర్ల్డ్ విల్ నెవ్ర్ సైపార్ట్, మెఽ బీ దిస్ విల్ ఓన్లీ మెఽక్ దై జాబ్ ఆవ్ ఇన్డీఐన్స్
బెట్ర్, సొ వాట్, దైట్ ఐలొన్ ఇస్ ఐ వర్దీ గొల్.


## ఐప్రొచ

క్రైన్ట్లీ ఆయ్ ఐమ్ యూసింగ్ [cmudict](https://github.కామ్/cmusphinx/cmudict), విచ
లిస్ట్స్ ఇంగ్గ్లిశ pronounciation కొడ్ ఫార్ సామ్ ౪౦-౫౦K వర్డ్స్. ఆయ్ ఐమ్ [మైపింగ్ దొస్
కొడ్స్ టూ Devanagari](https://github.కామ్/amitu/brahmic/బ్లాబ్/మైస్ట్ర్/సీఎమ్యూ.py#L౨౫-L౬౮).



## రిసాల్ట్ సొ ఫార్

దై సెకైన్డ్ హైఫ్ ఆవ్ దిస్ పెఽజ్ ఇస్ ఆటొ transliterated విద సిరొ మైన్యుఐల్ క్రెక్శైన్
యూసింగ్ దిస్ టూల్.

లూక్ ఐట్ [దై జిస్ట్](https://జిస్ట్.github.కామ్/amitu/౪౭e౮౪౩౮౩౨౧d౦b౯e౪b౩cd) విచ
శొస్ దై కైన్వ్ర్సైన్ ఆవ్ ౧౦౦౦ మొస్ట్ ఫ్రీక్వైన్ట్లీ యూస్డ్ వర్డ్స్ ఇన్ ఇంగ్గ్లిశ లైంగ్గ్వైజ్. ఇట్
ఇస్ ఓన్లీ ౭౦-౮౦% ఐక్య్రైట్ సొ ఫార్. ఈవిన్ దై ఐక్య్రైసీ రెఽట్ ఇస్ నాట్ నొన్, ఐస్ ఆయ్ ఐమ్ నాట్
దైట్ గ్రెఽట్ ఇన్ ఇంగ్గ్లిశ ప్రొన్ఽన్సీఎఽశైన్ మాయ్సెల్ఫ్.

## హెల్ప్ మీ ప్లీస్!

ఫార్క్ దై [జిస్ట్](https://జిస్ట్.github.కామ్/amitu/౪౭e౮౪౩౮౩౨౧d౦b౯e౪b౩cd), ఐన్డ్ క్రెక్ట్
ఇట్, ఐన్డ్ సెన్డ్ మీ ఐ మెఽల్. ఆర్ మెఽ బీ జాస్ట్ మార్క్ దై లాయ్న్స్ యూ థింగ్క్ ఆర్ రాంగ్.

ఎనీ హెల్ప్ విద ఫిక్సింగ్ సీఎమ్యూ.py ఇస్ హాయ్లీ ఐప్రీశీఎఽటిడ్ టూ.

