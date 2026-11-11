import React from 'react';
import {Composition, continueRender, delayRender, staticFile} from 'remotion';
import {Main} from './Main';

const FONTS: [string, string, string, string][] = [
	['Inter', 'fonts/Inter-400.woff2', '400', 'normal'],
	['Inter', 'fonts/Inter-500.woff2', '500', 'normal'],
	['Inter', 'fonts/Inter-600.woff2', '600', 'normal'],
	['Inter', 'fonts/Inter-700.woff2', '700', 'normal'],
	['Playfair Display', 'fonts/PlayfairDisplay-Italic.ttf', '400 900', 'italic'],
];
const handle = delayRender('fonts');
Promise.all(
	FONTS.map(([family, file, weight, style]) => {
		const face = new FontFace(family, `url(${staticFile(file)})`, {weight, style});
		return face.load().then((loaded) => document.fonts.add(loaded));
	}),
).then(() => continueRender(handle));

export const RemotionRoot: React.FC = () => (
	<Composition id="Main" component={Main} durationInFrames={1002} fps={30} width={1080} height={1920} />
);
