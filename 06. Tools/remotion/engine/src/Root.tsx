import {Composition, staticFile} from 'remotion';
import {Test} from './Test';
import {CaseReel, CaseReelProps, FPS, Reel} from './CaseReel/CaseReel';

// Default reel spec: 9:16, 1080x1920. CaseReel reads the project from --public-dir (reel.json sets the length).
export const RemotionRoot: React.FC = () => (
  <>
    <Composition id="Test" component={Test} width={1080} height={1920} fps={30} durationInFrames={60} />
    <Composition id="CaseReel" component={CaseReel} width={1080} height={1920} fps={FPS} durationInFrames={1}
      defaultProps={{green: false, reel: null} as CaseReelProps}
      calculateMetadata={async ({props}) => {
        const reel: Reel = await fetch(staticFile('reel.json')).then((r) => r.json());
        return {durationInFrames: reel.frames, props: {...props, reel}};
      }} />
  </>
);
