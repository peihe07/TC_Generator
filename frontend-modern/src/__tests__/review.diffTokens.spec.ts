import { describe, it, expect } from 'vitest';

import {
  diffTokens,
  tokenize,
  type DiffToken,
} from '../components/modules/review/diffTokens';

/**
 * Pure-function tests for the LCS-based word diff used by RegenDiff.
 * No React / DOM — just verifying the token streams.
 */
describe('tokenize', () => {
  it('keeps spaces and punctuation as their own tokens', () => {
    expect(tokenize('hello world')).toEqual(['hello', ' ', 'world']);
    expect(tokenize('a, b.')).toEqual(['a', ',', ' ', 'b', '.']);
  });

  it('returns empty array for empty string', () => {
    expect(tokenize('')).toEqual([]);
  });

  it('splits on common punctuation while keeping it', () => {
    expect(tokenize('foo(bar)')).toEqual(['foo', '(', 'bar', ')']);
  });
});

describe('diffTokens', () => {
  const textsOf = (tokens: DiffToken[], type: DiffToken['type']) =>
    tokens.filter((t) => t.type === type).map((t) => t.text);

  it('returns all same tokens for identical input', () => {
    const { left, right } = diffTokens('hello world', 'hello world');
    expect(left.every((t) => t.type === 'same')).toBe(true);
    expect(right.every((t) => t.type === 'same')).toBe(true);
    expect(textsOf(left, 'same').join('')).toBe('hello world');
  });

  it('marks pure additions as add on the right side', () => {
    const { left, right } = diffTokens('hello', 'hello world');
    expect(textsOf(left, 'del')).toEqual([]);
    // "hello" stays same on the left
    expect(textsOf(left, 'same')).toEqual(['hello']);
    // " " + "world" are added on the right
    expect(textsOf(right, 'add').join('')).toBe(' world');
  });

  it('marks pure deletions as del on the left side', () => {
    const { left, right } = diffTokens('hello world', 'hello');
    expect(textsOf(right, 'add')).toEqual([]);
    expect(textsOf(right, 'same')).toEqual(['hello']);
    expect(textsOf(left, 'del').join('')).toBe(' world');
  });

  it('handles a word replacement (mixed add + del)', () => {
    const { left, right } = diffTokens('foo bar', 'foo baz');
    expect(textsOf(left, 'same')).toEqual(['foo', ' ']);
    expect(textsOf(right, 'same')).toEqual(['foo', ' ']);
    expect(textsOf(left, 'del')).toEqual(['bar']);
    expect(textsOf(right, 'add')).toEqual(['baz']);
  });

  it('handles empty strings on either side', () => {
    const a = diffTokens('', 'abc');
    expect(textsOf(a.left, 'del')).toEqual([]);
    expect(textsOf(a.right, 'add')).toEqual(['abc']);

    const b = diffTokens('abc', '');
    expect(textsOf(b.left, 'del')).toEqual(['abc']);
    expect(textsOf(b.right, 'add')).toEqual([]);

    const c = diffTokens('', '');
    expect(c.left).toEqual([]);
    expect(c.right).toEqual([]);
  });

  it('reconstructs both original and new text from the streams', () => {
    const oldText = 'The quick brown fox jumps.';
    const newText = 'The quick red fox leaps!';
    const { left, right } = diffTokens(oldText, newText);

    // left should contain "same" + "del" tokens that reconstruct oldText
    const rebuiltOld = left
      .filter((t) => t.type === 'same' || t.type === 'del')
      .map((t) => t.text)
      .join('');
    expect(rebuiltOld).toBe(oldText);

    // right should contain "same" + "add" tokens that reconstruct newText
    const rebuiltNew = right
      .filter((t) => t.type === 'same' || t.type === 'add')
      .map((t) => t.text)
      .join('');
    expect(rebuiltNew).toBe(newText);
  });
});
