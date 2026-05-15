type ChatInputProps = {
  value: string
  placeholder: string
  loading: boolean

  onChange: (
    event: React.ChangeEvent<HTMLInputElement>
  ) => void

  onSend: () => void
}

export function ChatInput({
  value,
  placeholder,
  loading,
  onChange,
  onSend
}: ChatInputProps) {
  return (
    <div
      style={{
        width: "100%",
        maxWidth: "950px",
        margin: "0 auto",
        position: "relative",
        zIndex: 2
      }}
    >
      <div
        style={{
          display: "flex",
          alignItems: "center",
          background: "rgba(255,255,255,0.82)",
          backdropFilter: "blur(16px)",
          borderRadius: "24px",
          border: "1px solid rgba(124,58,237,0.16)",
          padding: "14px 20px",
          boxShadow:
            "0 18px 44px rgba(79,70,229,0.14)"
        }}
      >
        <input
          value={value}
          disabled={loading}
          onChange={onChange}
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              onSend()
            }
          }}
          placeholder={placeholder}
          style={{
            flex: 1,
            border: "none",
            outline: "none",
            background: "transparent",
            fontSize: "16px",
            color: "#1a1a1a"
          }}
        />

        <button
          disabled={loading}
          onClick={onSend}
          style={{
            width: "48px",
            height: "48px",
            borderRadius: "50%",
            border: "none",
            background:
              "linear-gradient(135deg, #7c3aed 0%, #2563eb 100%)",
            color: "#fff",
            cursor: "pointer",
            fontSize: "20px",
            opacity: loading ? 0.7 : 1
          }}
        >
          {loading ? "..." : "➜"}
        </button>
      </div>
    </div>
  )
}
