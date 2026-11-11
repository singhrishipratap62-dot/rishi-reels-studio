import * as React from "react";

/** The gradnext wordmark, drawn from the guideline artwork. Never retype it. */
export interface WordmarkProps {
  /** Ink: rhino on white, white on dark grounds, midnight for the small header mark, ink follows the theme. Default "rhino". */
  tone?: "rhino" | "white" | "midnight" | "ink";
  /** Rendered height in px; width keeps the 587:156 ratio. Default 32. */
  height?: number;
  className?: string;
}
export declare function Wordmark(props: WordmarkProps): React.ReactElement;

/** Text button. One primary per view. */
export interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  /** primary = Chrome Yellow, secondary = Periwinkle, ghost = outlined ink. Default "primary". */
  variant?: "primary" | "secondary" | "ghost";
  children: React.ReactNode;
}
export declare function Button(props: ButtonProps): React.ReactElement;

/** A brand value or pillar on a dark ground, with the periwinkle under-glow. */
export interface ValueCardProps {
  /** Two to four words, e.g. "Clarity Over Complexity". */
  children: React.ReactNode;
  className?: string;
}
export declare function ValueCard(props: ValueCardProps): React.ReactElement;

/** One approved colour-overlay pairing: a square fill on a square ground. */
export interface OverlayTileProps {
  /** dusk = background-01, white, mist = white with periwinkle corners, night = rhino-950 with periwinkle glows. Default "dusk". */
  ground?: "dusk" | "white" | "mist" | "night";
  /** The overlaid square. Default "yellow". */
  fill?: "yellow" | "white" | "periwinkle" | "midnight";
  /** Side in px. Default 160. */
  size?: number;
  /** Accessible name when the tile carries meaning. */
  label?: string;
  className?: string;
}
export declare function OverlayTile(props: OverlayTileProps): React.ReactElement;

/** gradnext beside a partner brand at equal weight. */
export interface PartnerLockupProps {
  /** divider = vertical rule, cross = "×", stacked = horizontal rule. Default "divider". */
  layout?: "divider" | "cross" | "stacked";
  /** The partner's logo element (an <img>) or name. Default placeholder "Partner Brand". */
  partner?: React.ReactNode;
  /** Wordmark ink. Default "midnight". */
  tone?: "rhino" | "white" | "midnight" | "ink";
  /** Wordmark height in px; match the partner logo's optical size. Default 32. */
  height?: number;
  className?: string;
}
export declare function PartnerLockup(props: PartnerLockupProps): React.ReactElement;
