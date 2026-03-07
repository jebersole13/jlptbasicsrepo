import { defineMiddleware, sequence } from 'astro:middleware';
import { AuthError } from './lib/auth';

const authMiddleware = defineMiddleware(async (context, next) => {
    const accessToken = context.cookies.get('access_token')?.value;
    const userEmail = context.cookies.get('user')?.value;

    context.locals.isAuthenticated = !!accessToken;
    context.locals.accessToken = accessToken;
    context.locals.refreshToken = context.cookies.get('refresh_token')?.value;
    context.locals.user = userEmail ?? '';

    return next();
});


const routeGuard = defineMiddleware(async (context, next) => {
    const { pathname } = context.url;
    const publicRoutes = new Set(['/', '/registration', '/registration/register_thanks', '/login', '/forgot']);
    const isPublic = publicRoutes.has(pathname) || pathname.startsWith('/reset');

    if (!isPublic && !context.locals.isAuthenticated) {
        return context.redirect('/login');
    }

    if ((pathname === '/login' || pathname === '/registration') && context.locals.isAuthenticated) {
        return context.redirect('/studypage/studydashboard');
    }

    try {
        return await next();
    } catch (error) {
        if (error instanceof AuthError) {
            context.cookies.delete('access_token', { path: '/' });
            context.cookies.delete('refresh_token', { path: '/' });
            context.cookies.delete('user', { path: '/' });
            return context.redirect('/login');
        }
        throw error;
    }
});

export const onRequest = sequence(authMiddleware, routeGuard);