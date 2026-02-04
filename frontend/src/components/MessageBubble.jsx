import React from 'react';

const MessageBubble = ({ role, content }) => {
    const isUser = role === 'user';

    return (
        <div className={`flex w-full mb-4 ${isUser ? 'justify-end' : 'justify-start'}`}>
            <div
                className={`max-w-[80%] rounded-2xl px-4 py-3 ${isUser
                        ? 'bg-blue-600 text-white rounded-br-none'
                        : 'bg-zinc-800 text-gray-100 rounded-bl-none border border-zinc-700'
                    }`}
            >
                <p className="whitespace-pre-wrap leading-relaxed">{content}</p>
            </div>
        </div>
    );
};

export default MessageBubble;
