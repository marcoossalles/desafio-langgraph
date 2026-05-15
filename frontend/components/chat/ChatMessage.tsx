type ChatMessageProps = {
  role: "user" | "assistant"
  content: string
}

export function ChatMessage({
  role,
  content
}: ChatMessageProps) {
  const isUser = role === "user"

  return (
    <div
      style={{
        width: "100%",
        display: "flex",
        justifyContent: isUser
          ? "flex-end"
          : "flex-start",
        marginBottom: "20px",
        position: "relative",
        zIndex: 2
      }}
    >
      <div
        style={{
          maxWidth: "70%",
          padding: "16px 20px",
          borderRadius: "24px",
          background: isUser
            ? "linear-gradient(135deg, #7c3aed 0%, #2563eb 100%)"
            : "rgba(255,255,255,0.86)",
          color: isUser
            ? "#ffffff"
            : "#111827",
          border: isUser
            ? "1px solid rgba(255,255,255,0.14)"
            : "1px solid rgba(124,58,237,0.1)",
          fontSize: "15px",
          lineHeight: 1.6,
          whiteSpace: "pre-wrap",
          wordBreak: "break-word",
          boxShadow:
            isUser
              ? "0 12px 28px rgba(37,99,235,0.22)"
              : "0 10px 24px rgba(79,70,229,0.08)"
        }}
      >
        {String(content)}
      </div>
    </div>
  )
}
