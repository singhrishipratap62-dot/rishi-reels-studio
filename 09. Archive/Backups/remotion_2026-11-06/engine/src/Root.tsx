import {Composition} from 'remotion';
import {Test} from './Test';

// Default reel spec: 9:16, 1080x1920, 30fps
export const RemotionRoot: React.FC = () => (
  <Composition id="Test" component={Test} width={1080} height={1920} fps={30} durationInFrames={60} />
);
