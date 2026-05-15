"use client"

import { useState } from "react"

import { sendMessage } from "@/services/api/chat.service"

import { ChatContainer } from "@/components/chat/ChatContainer"
import { ChatHeader } from "@/components/chat/ChatHeader"
import { ChatInput } from "@/components/chat/ChatInput"
import { ChatMessages } from "@/components/chat/ChatMessages"

type Message = {
  role: "user" | "assistant"
  content: string
}

export default function ChatPage() {
  const [message, setMessage] = useState("")
  const [messages, setMessages] =
    useState<Message[]>([])

  const [loading, setLoading] =
    useState(false)

  async function handleSendMessage() {
    if (!message.trim() || loading) return

    const currentMessage = message.trim()

    const userMessage: Message = {
      role: "user",
      content: currentMessage
    }

    setMessages((prev) => [
      ...prev,
      userMessage
    ])

    setMessage("")

    setLoading(true)

    try {
      const response = await sendMessage(
        currentMessage
      )

      const answer =
        response.answer ||
        response.final_response ||
        response.response ||
        "Nenhuma resposta encontrada."

      const assistantMessage: Message = {
        role: "assistant",
        content: answer
      }

      setMessages((prev) => [
        ...prev,
        assistantMessage
      ])
    } catch (error) {
      console.error(error)

      const errorMessage: Message = {
        role: "assistant",
        content:
          "Erro ao processar mensagem."
      }

      setMessages((prev) => [
        ...prev,
        errorMessage
      ])
    } finally {
      setLoading(false)
    }
  }
  return (
    <ChatContainer>
      {messages.length === 0 && (
        <ChatHeader title="🎬 AI Movie" />
      )}

      <ChatMessages
        messages={messages}
        loading={loading}
      />

      <ChatInput
        value={message}
        loading={loading}
        onChange={(e) =>
          setMessage(e.target.value)
        }
        onSend={handleSendMessage}
        placeholder="Pergunte sobre filmes, atores ou recomendações"
      />
    </ChatContainer>
  )
}
