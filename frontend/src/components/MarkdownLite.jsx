// Lightweight markdown: bold (**text**) and bullet lists (• text) only —
// the model output never uses anything beyond that, so a full markdown
// library would be dead weight.
function renderInline(text, keyBase) {
  const parts = text.split(/(\*\*[^*]+\*\*)/g);
  return parts.map((part, i) =>
    part.startsWith("**") && part.endsWith("**") && part.length > 4 ? (
      <strong key={`${keyBase}-${i}`}>{part.slice(2, -2)}</strong>
    ) : (
      part
    )
  );
}

function toBlocks(text) {
  const lines = text.split(/\r?\n/);
  const blocks = [];
  let paraLines = [];

  const flushPara = () => {
    if (paraLines.length) {
      blocks.push({ type: "p", lines: paraLines });
      paraLines = [];
    }
  };

  for (const rawLine of lines) {
    const line = rawLine.trim();
    const bulletMatch = line.match(/^[•]\s*(.*)$/);
    if (bulletMatch) {
      flushPara();
      const last = blocks[blocks.length - 1];
      if (last && last.type === "ul") {
        last.items.push(bulletMatch[1]);
      } else {
        blocks.push({ type: "ul", items: [bulletMatch[1]] });
      }
    } else if (line === "") {
      flushPara();
    } else {
      paraLines.push(line);
    }
  }
  flushPara();
  return blocks;
}

export default function MarkdownLite({ text }) {
  const blocks = toBlocks(text || "");
  return (
    <>
      {blocks.map((block, bi) =>
        block.type === "ul" ? (
          <ul className="msg-list" key={bi}>
            {block.items.map((item, ii) => (
              <li key={ii}>{renderInline(item, `${bi}-${ii}`)}</li>
            ))}
          </ul>
        ) : (
          <p className="msg-para" key={bi}>
            {block.lines.map((line, li) => (
              <span key={li}>
                {renderInline(line, `${bi}-${li}`)}
                {li < block.lines.length - 1 && <br />}
              </span>
            ))}
          </p>
        )
      )}
    </>
  );
}
