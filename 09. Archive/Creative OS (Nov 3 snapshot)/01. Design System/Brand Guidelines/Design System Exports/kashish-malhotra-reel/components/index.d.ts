/** One caption word, timed in seconds from the SRT. hl = holds a number or %, shown in caption-highlight. */
export interface CaptionWord { w: string; t: number; e: number; hl: boolean }
/** One on-screen line. join = the next phrase follows within 0.6s, so the pill stays and morphs. */
export interface CaptionPhrase { t0: number; end: number; hide: number; join: boolean; words: CaptionWord[] }
export interface RisingCaptionProps {
  /** Split an SRT into words; fixes maps mis-heard words to the right ones, e.g. {"tabbed":"capped"}. */
  wordsFromSrt(srt: string, fixes?: Record<string, string>): CaptionWord[];
  /** Group words into one-line phrases (about 20 characters). end = the film's last second, so the last pill stays up. */
  phrasesFromWords(words: CaptionWord[], end?: number): CaptionPhrase[];
  /** Build the caption layer in a 1080x1920 host and return render(t), pure in t seconds. */
  mount(host: HTMLElement, phrases: CaptionPhrase[]): (t: number) => void;
}
