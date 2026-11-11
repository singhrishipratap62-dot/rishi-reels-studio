import {AbsoluteFill, interpolate, useCurrentFrame} from 'remotion';

export const Test: React.FC = () => {
  const frame = useCurrentFrame();
  const opacity = interpolate(frame, [0, 20], [0, 1], {extrapolateRight: 'clamp'});
  return (
    <AbsoluteFill style={{backgroundColor: '#111', justifyContent: 'center', alignItems: 'center'}}>
      <div style={{color: 'white', fontSize: 120, fontWeight: 800, opacity}}>Remotion OK</div>
    </AbsoluteFill>
  );
};
