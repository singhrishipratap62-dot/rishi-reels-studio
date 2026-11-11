// Caption groups in edit seconds (roughcut_v3), from Rishi's SRT mapped through cutlist_v3.csv.
// Word markers: *word* = Playfair italic, **word** = bold.
export type Group = {s: number; text: string};

export const GROUPS: Group[] = [
	{s: 0.17, text: '*Claude* mein video daal'},
	{s: 0.81, text: 'ke yeh prompt daal'},
	{s: 1.41, text: 'doge toh aisa kuch'},
	{s: 2.19, text: 'ban jaayega.'},
	{s: 2.83, text: 'Aisa kuch **nahi** hota hai.'},
	{s: 4.1, text: ''}, // ink drum-roll carries the words
	{s: 5.27, text: 'Aap duniya bhar ki *skills*'},
	{s: 6.27, text: 'ikattha kar lo, GitHub'},
	{s: 7.01, text: '*repos* ikattha kar lo.'},
	{s: 8.17, text: 'Jab tak aap Claude ko apna'},
	{s: 9.11, text: '*taste* ya design skill'},
	{s: 9.99, text: 'nahi samjha paoge,'},
	{s: 10.71, text: 'woh aapke liye kuch *ghanta*'},
	{s: 11.47, text: 'achha edit nahi karne wala hai.'},
	{s: 12.46, text: 'And yeh poori video bhi'},
	{s: 13.35, text: '**end-to-end** Claude se *edited* hai.'},
	{s: 14.42, text: 'Why does this look'},
	{s: 15.28, text: '*better* than all the Claude'},
	{s: 16.38, text: '**slop** which you see out there?'},
	{s: 17.43, text: 'Because maine usko *samjhaya* hai.'},
	{s: 18.51, text: 'Pehli baar mein aapko usko'},
	{s: 19.25, text: 'mehnat se samjhana hai'},
	{s: 19.93, text: 'ki *kya* karna hai,'},
	{s: 20.49, text: '*kaise* karna hai,'},
	{s: 20.91, text: 'aur ek baar woh samajh gaya,'},
	{s: 21.87, text: 'kuch *iterations* ke baad,'},
	{s: 23.04, text: 'it will get so better that'},
	{s: 24.24, text: 'it can do the whole thing'},
	{s: 25.14, text: '*autonomously* without your intervention.'},
	{s: 26.82, text: 'And if you want to learn'},
	{s: 28.03, text: 'how I did this,'},
	{s: 29.03, text: 'comment **EDIT** and I will'},
	{s: 30.05, text: 'send you a *step-by-step*'},
	{s: 30.99, text: 'breakdown of how you can'},
	{s: 32.07, text: 'achieve these kind of results.'},
];
export const END_S = 33.38;

// Drum-roll words for the ink beat (edit seconds).
export const DRUM = [
	{s: 4.1, w: 'This', i: false},
	{s: 4.23, w: "doesn't", i: false},
	{s: 4.49, w: 'work', i: false},
	{s: 4.68, w: 'like that.', i: true},
];
